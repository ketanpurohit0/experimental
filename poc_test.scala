// set HADOOP_HOME=C:\MyInstalled\spark-2.4.5-bin-hadoop2.7\spark-2.4.5-bin-hadoop2.7

import org.apache.spark.sql.SparkSession
import spark.implicits._

val sparkSession = SparkSession.builder().appName("POC").getOrCreate()

val leftDf = spark.read.json("C:/MyWork/python/gitBusinessRulesEngine/people.json")
leftDf.printSchema()