ThisBuild / scalaVersion := "2.12.7"
ThisBuild / organization := "com.example"

lazy val POC = (project in file("."))
  .settings(
    name := "POC"
  )

