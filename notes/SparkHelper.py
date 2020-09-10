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
        df = df.withColumn(cn, regexp_replace(col(cn), '^\s+', brv))

    return df


def compare(sparkSession, leftDf, rightDf, tolerance, keys):
    return leftDf