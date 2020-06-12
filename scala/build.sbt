ThisBuild / scalaVersion := "2.12.7"
ThisBuild / organization := "com.example"

lazy val POC = (project in file("."))
  .settings(
    name := "POC"
  )
  
val sparkVersion = "2.4.2"

libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % sparkVersion,
  "org.apache.spark" %% "spark-sql" % sparkVersion
)
