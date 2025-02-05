error id: 
file://<WORKSPACE>/build.sbt
empty definition using pc, found symbol in pc: 
empty definition using semanticdb
|empty definition using fallback
non-local guesses:
	 -sparkVersion.
	 -sparkVersion#
	 -sparkVersion().
	 -scala/Predef.sparkVersion.
	 -scala/Predef.sparkVersion#
	 -scala/Predef.sparkVersion().

Document text:

```scala
ThisBuild / version := "0.1.0-SNAPSHOT"

ThisBuild / scalaVersion := "2.13.12"

lazy val root = (project in file("."))
  .settings(
    name := "spark-video-course"
  )

val sparkVersion = "3.5.0"

libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % sparkVersion,
  "org.apache.spark" %% "spark-sql" % sparkVersion
)
```

#### Short summary: 

empty definition using pc, found symbol in pc: 