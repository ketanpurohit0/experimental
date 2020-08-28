import SparkHelper as sh

# - Investigate NULL vs '-' and NULL vs 1900-01-01 comparison
# SQL Code
# - Spark code
sparkSession = sh.getSpark()
sparkSession.sparkContext.setLogLevel("ERROR")
# URL
url = sh.getUrl('postgres','postgres','foobar_secret')

q1 = "SELECT * FROM tslp"
q2 = "SELECT * FROM tetl"
df1 = sh.getQueryDataFrame(sparkSession, url, q1)
df2 = sh.getQueryDataFrame(sparkSession, url, q2)

df1.show()
df2.show()

df1.dtypes
df2.dtypes

# null default map per column name
nullDefaultMap={'c_str':'-', 'c_dt':'1900-01-01', 'c_ts' : '1900-01-01 00:00:00','c_num' : 0, 'c_f' : '0.0', 'n1':'1', 'n2':'2', 'n3':'4','n4':'8', 'n5':'16', 'b':'False', 'tx':'Text'}

# apply defaults for null
t=df1.na.fill(nullDefaultMap)
t.dtypes
t.show()
