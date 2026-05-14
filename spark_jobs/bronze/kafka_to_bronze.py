from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json

from spark_jobs.schemas.ecommerce_schema import ecommerce_schema

# Create Spark Session
spark = (
    SparkSession.builder
    .appName("KafkaToBronze")
    .config(
    "spark.jars.packages",
    ",".join([
        "org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.1",
        "io.delta:delta-spark_2.12:3.1.0"
    ])
)
    .getOrCreate()
)

spark.sparkContext.setLogLevel("WARN")

# Read stream from Kafka
raw_df = (
    spark.readStream
    .format("kafka")
    .option("kafka.bootstrap.servers", "localhost:9092")
    .option("subscribe", "ecommerce-events")
    .option("startingOffsets", "earliest")
    .load()
)

# Convert Kafka binary value to string
kafka_df = raw_df.selectExpr("CAST(value AS STRING) as json_data")

# Parse JSON using schema
parsed_df = (
    kafka_df
    .select(
        from_json(
            col("json_data"),
            ecommerce_schema
        ).alias("data")
    )
    .select("data.*")
)

# Write stream to console for testing
console_query = (
    parsed_df.writeStream
    .format("console")
    .outputMode("append")
    .option("truncate", False)
    .start()
)

# Write stream to Bronze layer
bronze_query = (
    parsed_df.writeStream
    .format("parquet")
    .outputMode("append")
    .option(
        "checkpointLocation",
        "spark_jobs/checkpoints/bronze_checkpoint"
    )
    .start("spark_jobs/output/bronze")
)

# Keep stream alive
spark.streams.awaitAnyTermination()