from pyspark.sql import SparkSession

standardNullReplacementMapPerStandardType = {
    "string": "-",
    "date": "1900-01-01",
    "timestamp": "1900-01-01 00:00:00",
    "double": "0.0",
    "int": "0",
    "boolean": "False",
}


def getSpark():
    return SparkSession.builder.appName("Test").getOrCreate()


def getUrl(db, user, secret):
    return f"jdbc:postgresql://localhost/{db}?user={user}&password={secret}"


def getReader(sparkSession, url):
    return (
        sparkSession.read.format("jdbc")
        .option("driver", "org.postgresql.Driver")
        .option("url", url)
    )


def getQueryDataFrame(sparkSession, url, query):
    reader = getReader(sparkSession, url).option("dbtable", f"({query}) T")
    df = reader.load()
    df = replaceNulls(df)
    df = replaceBlanks(df)
    return df


def getStandardizedType(dfType):
    if (
        dfType == "string"
        or dfType == "date"
        or dfType == "timestamp"
        or dfType == "double"
        or dfType == "int"
        or dfType == "boolean"
    ):
        return dfType
    elif "decimal" in dfType:
        return "double"
    else:
        return "int"


def replaceNulls(df):
    nullReplacementMap = {
        cn: standardNullReplacementMapPerStandardType.get(getStandardizedType(ct))
        for (cn, ct) in df.dtypes
    }
    return df.na.fill(nullReplacementMap)


def replaceBlanks(df):
    from pyspark.sql.functions import col, when, lit, regexp_replace

    brv = standardNullReplacementMapPerStandardType.get("string", "")
    stringCols = [cn for (cn, ct) in df.dtypes if ct == "string"]
    for cn in stringCols:
        df = df.withColumn(cn, when(col(cn) == "", brv).otherwise(col(cn)))
        df = df.withColumn(cn, regexp_replace(col(cn), "^\s+", brv))

    return df


def compareDfs(sparkSession, leftDf, rightDf, tolerance, keysLeft, keysRight, colExcludeList, joinType):
    from pyspark.sql.functions import col, abs, lit

    (leftSide_tag, rightSide_tag, boolCol_tag) = ("_left", "_right", "_same")
    joinConditionsAsList = makeDfJoinCondition(
        leftDf, rightDf, tolerance, keysLeft, keysRight
    )
    joinConditionAsString = joinCondAsString(joinConditionsAsList)
    joinConditionObject = compileAndEval(joinConditionAsString, leftDf, rightDf)
    (
        colsInBoth,
        colsInLeftOnly,
        colsInRightOnly,
        allLeftCols,
        allRightCols,
    ) = getDfColsInfo(leftDf, rightDf)

    newColNamesLeft = getNewColsNames(allLeftCols, leftSide_tag)
    newColNamesRight = getNewColsNames(allRightCols, rightSide_tag)
  
    colDictOldNameToNewNames = {}
    for item in colsInLeftOnly:
        colDictOldNameToNewNames[item] = (f"{item}{leftSide_tag}", None, None)
    for item in colsInRightOnly:
        colDictOldNameToNewNames[item] = (None, f"{item}{leftSide_tag}", None)

    newColNamesAll = list(newColNamesLeft)
    newColNamesAll.extend(newColNamesRight)

    # join the two dfs using joinType (suggest full_outer)
    df = (leftDf.join(rightDf, joinConditionObject, joinType)
          .toDF(*newColNamesAll)
          .select(*sorted(newColNamesAll)))

    # create new column "PASS" which initially will be true but will be re-evaluated based on individual columns
    df = df.withColumn("PASS", lit(True))

    # now add a new column to hold compare results for side by side diff
    # we can only do this for columns that exist both sides
    dictOfColDTypes = dict(df.dtypes)
    colsToCompare = list(colsInBoth)
    for colInBoth in colsToCompare:
        leftCol = f"{colInBoth}{leftSide_tag}"
        rightCol = f"{colInBoth}{rightSide_tag}"
        newBoolCol = f"{colInBoth}{boolCol_tag}"
        if (colInBoth in colExcludeList):
            df = df.withColumn(newBoolCol, lit(True))
        else:
            if leftCol in dictOfColDTypes:
                leftColType = dictOfColDTypes[leftCol]
                righColType = dictOfColDTypes[rightCol]
                if (isDoubleType(leftColType, righColType)):
                    df = df.withColumn(newBoolCol, abs(col(leftCol) - col(rightCol)) < tolerance)
                else:
                    df = df.withColumn(newBoolCol, col(leftCol) == col(rightCol))

        colDictOldNameToNewNames[colInBoth] = (leftCol, rightCol, newBoolCol)
        df.withColumn("PASS", col("PASS") & col(newBoolCol))
        newColNamesAll.append(newBoolCol)

        # - return data in its natural order list (ie the order as it existed in original dataframes)
    naturalOrderList = ["PASS"]
    for item in colsInBoth:
        tup = colDictOldNameToNewNames.get(item)
        naturalOrderList.extend(list(tup))
    for item in colsInLeftOnly:
        (a, b, c) = colDictOldNameToNewNames.get(item)
        naturalOrderList.append(a)
    for item in colsInRightOnly:
        (a, b, c) = colDictOldNameToNewNames.get(item)
        naturalOrderList.append(b)
    df = df.select(*naturalOrderList)

    return df


def getNewColsNames(columnNameList, tag):
    return [f"{x}{tag}" for x in columnNameList]


def joinCondAsString(joinConditionAsList):
    conditions = [x for x in joinConditionAsList if not (x == "" or x == "None" or x is None)]
    code = ",".join(conditions)
    code = f"[{code}]"
    return code


def compileAndEval(codeStr, leftDf, rightDf):
    # leftDf and rightDf are required to provide local context for eval
    compiledCode = compile(codeStr, "<string>", "eval")
    return eval(compiledCode)


def getDfColsInfo(leftDf, rightDf):
    # order is important
    colsInBoth = [x for x in leftDf.columns if x in rightDf.columns]
    colsInLeftOnly = [x for x in leftDf.columns if x not in rightDf.columns]
    colsInRightOnly = [x for x in rightDf.columns if x not in leftDf.columns]
    allLeftCols = list(leftDf.columns)
    allRightCols = list(rightDf.columns)
    return (colsInBoth, colsInLeftOnly, colsInRightOnly, allLeftCols, allRightCols)


def makeDfJoinCondition(leftDf, rightDf, tolerance, keysLeft, keysRight):
    leftTypesMap = dict(leftDf.dtypes)
    rightTypesMap = dict(rightDf.dtypes)
    leftKeysList = [x.strip() for x in keysLeft.split(",")]
    rightKeysList = [x.strip() for x in keysRight.split(",")]
    keyByKey = zip(leftKeysList, rightKeysList)
    conditions = [
        makeDfConditionWithTolerance(
            lname, leftTypesMap[lname], rname, rightTypesMap[rname], tolerance
        )
        for (lname, rname) in keyByKey
    ]
    return conditions


def makeDfConditionWithTolerance(leftColName, leftColType, rightColName, rightColType, tolerance):
    if (isDoubleType(leftColType, rightColType)):
        return makeDoubleJoinCond(leftColName, rightColName, tolerance)
    else:
        return makeNormalJoinCond(leftColName, rightColName)


def isDoubleType(leftColType, rightColType):
    listDoubleType = ["double", "decimal"]
    return leftColType in listDoubleType or rightColType in listDoubleType


def makeDoubleJoinCond(leftColName, rightColName, tolerance):
    innerTolerance = tolerance + 0.000001
    return (f"(leftDf['{leftColName}'] - rightDf['{rightColName}']).between({-innerTolerance},{innerTolerance})")


def makeNormalJoinCond(leftColName, rightColName):
    return(f"leftDf['{leftColName}'] == rightDf['{rightColName}']")