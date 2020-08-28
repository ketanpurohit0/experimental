import SparkHelper as sh

sparkSession = sh.getSpark()
sparkSession.sparkContext.setLogLevel("ERROR")
# URL
url = sh.getUrl('postgres','postgres','foobar_secret')

q1 = "SELECT * FROM foo_left"
q2 = "SELECT * FROM foo_right"
df1 = sh.getQueryDataFrame(sparkSession, url, q1)
df2 = sh.getQueryDataFrame(sparkSession, url, q2)

# Do an outer join
dfj = df1.join(df2, df1.name_left == df2.name_right, 'full_outer')
dfj.show()
# Now we have outer join where rows havent matched, but some have
# so extract the misses.
left_cols_only = [x for x in dfj.columns if 'left' in x]
df1miss = dfj.select(left_cols_only).filter("name_right is null")
right_cols_only = [x for x in dfj.columns if 'right' in x]
df2miss = dfj.select(right_cols_only).filter("name_left is null")
df1miss.show()
df2miss.show()
# We remove the misses from original frame (we only keep the good records
dfj = dfj.filter('name_left is not null and name_right is not null')
dfj.show()
# Now  'normalise' name on both sides of the misses
from pyspark.sql.functions import regexp_replace, col
df1miss = df1miss.withColumn('name_left', regexp_replace( col('name_left'), '(_[0-9]*_|_[0-9]*$)','@CX@'))
df2miss = df2miss.withColumn('name_right', regexp_replace( col('name_right'), '(_[0-9]*_|_[0-9]*$)','@CX@'))
df1miss.show()
df2miss.show()
# Attempt join again on the misses subset, this time with additional columns
# as the keys
dfj2 = df1miss.join(df2miss, [df1miss.name_left == df2miss.name_right, df1miss.uid_left == df2miss.uid_right], 'full_outer')
dfj2.show()
# Take a union
dfj3 = dfj.union(dfj2)
dfj3.show()

sparkSession.stop()


	