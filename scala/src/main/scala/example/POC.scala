// set HADOOP_HOME=C:/MyInstalled/spark-2.4.5-bin-hadoop2.7/spark-2.4.5-bin-hadoop2.7
// .\bin\spark-sql -f C:/MyWork/python/gitBusinessRulesEngine/poc_test.scala
// .\bin\spark-submit C:\MyWork\python\gitBusinessRulesEngine\scala\target\scala-2.12\poc_2.12-0.1.0-SNAPSHOT.jar

import org.apache.poi.ss.usermodel.{ DataFormatter, WorkbookFactory, Row }
import java.io.File
import collection.JavaConversions._ 
import org.apache.spark.sql.DataFrame
import org.apache.spark.sql.Row


object POC {
    def main(args: Array[String]): Unit = {
        println("Hello, world - Ketan")
		
		//readExcel("C:/MyWork/python/gitBusinessRulesEngine/scala/src/main/scala/example/dataresource/Example.xlsx")
readExcel("Example.xlsx")

    }
	
	def stuff() = {
	
	import org.apache.spark.sql.SparkSession

	val sparkSession = SparkSession.builder().appName("POC").getOrCreate()
	
	import sparkSession.implicits._
	//import scala.io.Source
	//val linecount = Source.fromFile("C:/MyWork/python/gitBusinessRulesEngine/scala/src/main/scala/example/dataresource/people.json").getLines.size
	//println(linecount)

	//import org.apache.spark.SparkFiles
	//val foo = SparkFiles.get("C:/MyWork/python/gitBusinessRulesEngine/scala/src/main/scala/example/dataresource/people.json") 
	//println(s"Path:$foo")
	//sparkSession.read.text(SparkFiles.get("C:/MyWork/python/gitBusinessRulesEngine/scala/src/main/scala/example/dataresource/people.json")).show

	val leftDf = sparkSession.read.json("C:/MyWork/python/gitBusinessRulesEngine/scala/src/main/scala/example/dataresource/people.json")
	leftDf.printSchema()
	val outFilePath = "C:/MyWork/python/gitBusinessRulesEngine/scala/src/main/scala/example/dataresource/people.csv"
	leftDf.write.format("csv").save(outFilePath)
	/*leftDf.coalesce(1)
      .write
      .option("header","true")
      .option("sep",",")
      .mode("overwrite")
      .csv(outFilePath)*/

	}
	

	
	
	def readExcel(file: String): DataFrame = {
	
	import org.apache.spark.{SparkConf, SparkContext}
	import org.apache.spark.sql.SparkSession
	val sparkConf = new SparkConf().setAppName("sparkbyexamples.com").setMaster("local[1]")
	val sparkContext = new SparkContext(sparkConf )
val sparkSession = SparkSession.builder().appName("POC").getOrCreate()
		sparkSession.read
    .format("com.crealytics.spark.excel")
    .option("location", file)
    .option("useHeader", "true")
    .option("treatEmptyValuesAsNulls", "true")
    .option("inferSchema", "true")
    .option("addColorColumns", "False")
    .load()
	}		

}
