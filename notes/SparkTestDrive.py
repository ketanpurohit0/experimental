import SparkHelper as sh

sparkSession = sh.getSpark()
sparkSession.sparkContext.setLogLevel("ERROR")
# QUERY
query = 'SELECT * FROM Foo'
# URL
url = sh.getUrl('postgres','postgres','foobar_secret')
# DF
df = sh.getQueryDataFrame(sparkSession, url, query)
df.show()
# Arrays (https://mungingdata.com/apache-spark/arraytype-columns/)
from pyspark.sql.functions import col
from pyspark.sql.functions import explode
df.select(col("name"), explode(col("moremetadata"))).show()
df.select(col("name"), explode(col("metadata"))).show()
# Len of array
from pyspark.sql.functions import size
df.select(col("metadata"),size(col("metadata"))).show()
# element_at
from pyspark.sql.functions import element_at
df.select(col("metadata"),element_at(col("metadata"),3)).show() # returns NULL if no element_at index
# concat
from pyspark.sql.functions import concat
df.select(col("metadata"), col("moremetadata"),concat(col("metadata"),col("moremetadata"))).show()
l = [col("metadata"), col("moremetadata")]
df.select(col("metadata"), col("moremetadata"),concat(*l)).show()
# JSON (https://stackoverflow.com/questions/41107835/pyspark-parse-a-column-of-json-strings)
from pyspark.sql.functions import lit,schema_of_json,from_json
json_schema = sparkSession.read.json(df.rdd.map(lambda row: row.js)).schema
df.withColumn('js', from_json(col('js'), json_schema)).show()

sparkSession.stop()
