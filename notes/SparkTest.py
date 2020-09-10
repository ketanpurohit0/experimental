from pyspark.sql import SparkSession
import SparkHelper as sh

# Run with pyspark or spark-submit
# --pyspark
# C:\MyInstalled\spark-2.4.5-bin-hadoop2.7\spark-2.4.5-bin-hadoop2.7\bin\pyspark --jars C:\MyWork\experimental\notes\postgresql-42.2.14.jar
# import SparkTest
# -- spark-submit
# spark-submit --jars C:\MyWork\experimental\notes\postgresql-42.2.14.jar SparkTest

sparkSession = sh.getSpark()
sparkSession.sparkContext.setLogLevel("ERROR")

url = sh.getUrl(db = "postgres", user = "postgres", pwd = "foobar_secret")

# Get base data
baseSql = "SELECT c1, c2, c_inbaseonly FROM table_V1"
dfBaseline = sh.getQueryDataFrame(sparkSession, url, baseSql)

# Get test data
testSql = "SELECT c1, c2, c_intargetonly FROM table_V2"
dfTest = sh.getQueryDataFrame(sparkSession, url, testSql)

# To a side by side compare
# c1_left, c1_right, c1_same, \
# c2_left, c2_right, c2_same, \
# c_inbaseonly, c_intargetonly
dfResult = sh.compare(sparkSession, dfBaseline, dfTest, tolerance=0.1, keys="c1,c2")

# now write to csv or parquet

sparkSession.stop()
