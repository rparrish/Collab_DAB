import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

print(f'Spark version{spark.version}')

