import org.apache.spark.sql.SparkSession
import spark.implicits._

val sparkSession = SparkSession.builder().appName("POC").getOrCreate()

val leftDf = spark.read.json("C:/MyWork/python/gitBusinessRulesEngine/people.json")
leftDf.printSchema() 