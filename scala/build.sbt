ThisBuild / scalaVersion := "2.12.7"
ThisBuild / organization := "com.example"

lazy val POC = (project in file("."))
  .settings(
    name := "POC"
  )
  
val sparkVersion = "2.4.2"

libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % sparkVersion,
  "org.apache.spark" %% "spark-sql" % sparkVersion,
  "org.apache.poi" % "poi" % "3.17",
  "org.apache.poi" % "poi-ooxml" % "3.17",
  "com.crealytics" % "spark-excel_2.11" % "0.8.2"
)
