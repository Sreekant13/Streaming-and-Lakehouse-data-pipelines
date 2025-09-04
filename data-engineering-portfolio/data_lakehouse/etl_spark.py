# data_lakehouse/etl_spark.py
# Batch ETL transform simulating AWS Glue locally using PySpark.
# Reads CSV, filters & normalizes, writes Parquet (lake zone).

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, when

RAW_PATH = "data/raw/nyc_taxi.csv"
OUT_PATH = "data/processed/nyc_taxi_parquet"

def main():
    spark = (SparkSession.builder
             .appName("LakehouseETL")
             .getOrCreate())
    spark.sparkContext.setLogLevel("WARN")

    df = (spark.read
                .option("header", True)
                .option("inferSchema", True)
                .csv(RAW_PATH))

    # Example cleaning
    df_clean = (df
        .filter(col("fare_amount").cast("double") > 0)
        .withColumn("tip_fraction",
                    (col("tip_amount").cast("double") / when(col("fare_amount") == 0, None).otherwise(col("fare_amount"))))
    )

    (df_clean.write.mode("overwrite").parquet(OUT_PATH))
    print(f"Wrote cleaned parquet to: {OUT_PATH}")

if __name__ == "__main__":
    main()