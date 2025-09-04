📊 Data Engineering Portfolio

This repository showcases two end-to-end data engineering projects designed to demonstrate production-style workflows in both real-time streaming and batch lakehouse paradigms.

The projects are lightweight, fully reproducible locally, and cover concepts like event streaming, ETL, orchestration, observability, and analytics.

1. Streaming Pipeline – Real-Time Analytics

Stack: Apache Kafka, Spark Structured Streaming, Python, Docker, (optional: Prometheus + Grafana)

Description

This project simulates IoT-style sensor events being streamed in real-time. Events are ingested into Kafka, processed with Spark Structured Streaming, and written to the console (or Parquet for persistence). Optional hooks are provided for Grafana dashboards via Prometheus metrics.
Steps to Run:

cd streaming_pipeline

# 1. Start Kafka broker & ZooKeeper
docker-compose up -d

# 2. Start producer to send events
pip install -r requirements.txt
python producer.py --bootstrap localhost:9092 --topic iot-events --rate 5

# 3. Run Spark consumer
spark-submit \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0 \
  spark_app.py

👉 You’ll see alert events streaming in the console when temperature > 35°C.
For persistence, you can replace the sink with a Parquet writer and integrate monitoring with Grafana.


2. Data Lakehouse – Batch Analytics

Stack: PySpark, Parquet, DuckDB, dbt (placeholder), Tableau/Superset

Description

This project demonstrates how to build a lakehouse-style architecture locally. Raw CSV data is cleaned and transformed with PySpark (simulating AWS Glue), stored in Parquet (data lake), and queried with DuckDB (simulating Athena/Redshift Spectrum). The dbt folder is included as a placeholder for curated models.

Steps to Run:
cd data_lakehouse

# 1. Place raw CSV into data/raw/
# Example: data/raw/nyc_taxi.csv

# 2. Run ETL to produce Parquet output
spark-submit etl_spark.py

# 3. Run DuckDB analytics queries
pip install duckdb
python duckdb_analytics.py


👉 Output: Aggregated results (e.g., average fare by passenger count) are printed to the console.
You can extend this by:

Adding dbt models for staging/curated layers

Connecting Tableau or Apache Superset for BI dashboards

Migrating storage to AWS S3 and running the same jobs with Glue + Athena


🛠 Tech Stack Coverage

# Streaming: Apache Kafka, Spark Structured Streaming
# Batch / Lakehouse: PySpark ETL, Parquet, DuckDB (Athena/Redshift simulation)
# Infra: Docker Compose for Kafka/ZooKeeper
# Monitoring: Prometheus + Grafana integration (optional extension)
# Orchestration: dbt placeholder included for curated data transformations