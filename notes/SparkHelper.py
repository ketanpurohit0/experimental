from pyspark.sql import SparkSession

standardNullReplacementMapPerStandardType = {'string':'-', 'date':'1900-01-01', 'timestamp':'1900-01-01 00:00:00', 'double':'0.0', 'int':'0', 'boolean':'False'}

def getSpark():
    ss = SparkSession.builder.appName("Test").getOrCreate()
    return ss

def getUrl(db, user, pwd):
    url = f"jdbc:postgresql://localhost/{db}?user={user}&password={pwd}"
    return url

def getReader(sparkSession,url):
    reader = sparkSession.read.format("jdbc").option("driver","org.postgresql.Driver").option("url", url)
    return reader

def getQueryDataFrame(sparkSession, url, query):
    reader = getReader(sparkSession, url).option("dbtable", f"({query}) T")
    return reader.load()
	
def getStandardizedType(dfType):
    if (dfType == 'string' or dfType == 'date' or dfType == 'timestamp' or dfType == 'double' or dfType == 'int' or dfType == 'boolean'):
        return dfType
    elif ('decimal' in dfType):
        return 'double'
    else:
        return 'int'
	
def replaceNulls(df):
    nullReplacementMap = {cn:standardNullReplacementMapPerStandardType.get(getStandardizedType(ct)) for (cn, ct) in df.dtypes}
    return df.na.fill(nullReplacementMap)
