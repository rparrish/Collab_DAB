
library(sparklyr)

sc <- spark_connect(method = "databricks")

spark_version(sc)

