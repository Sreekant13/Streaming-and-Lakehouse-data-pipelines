# streaming_pipeline/spark_app.py
# Spark Structured Streaming consumer reading 'iot-events' and flagging high-temp alerts.
# Requires: pyspark
#
# Example run:
#   spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0 spark_app.py

from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col, expr
from pyspark.sql.types import StructType, StructField, IntegerType, DoubleType, StringType

KAFKA_BOOTSTRAP = "localhost:9092"
TOPIC = "iot-events"

schema = StructType([
    StructField("device_id", IntegerType(), True),
    StructField("temp_c", DoubleType(), True),
    StructField("humidity", DoubleType(), True),
    StructField("ts", StringType(), True),
])

def main():
    spark = (SparkSession.builder
             .appName("StreamingAlerts")
             .getOrCreate())

    spark.sparkContext.setLogLevel("WARN")

    raw = (spark.readStream
           .format("kafka")
           .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP)
           .option("subscribe", TOPIC)
           .option("startingOffsets", "latest")
           .load())

    parsed = (raw.selectExpr("CAST(value AS STRING) as json_str")
                  .select(from_json(col("json_str"), schema).alias("data"))
                  .select("data.*"))

    # Simple rule: temp > 35C => alert
    alerts = parsed.withColumn("is_alert", col("temp_c") > expr("35.0"))

    # Write to console (for demo). Replace with S3/Parquet sink for persistence.
    query = (alerts.writeStream
                   .format("console")
                   .outputMode("append")
                   .option("truncate", False)
                   .start())

    query.awaitTermination()

if __name__ == "__main__":
    main()