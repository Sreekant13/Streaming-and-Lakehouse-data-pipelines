# Streaming Pipeline (Kafka + Spark Structured Streaming)

Minimal real-time analytics demo that ingests JSON events into **Kafka**, processes them with **Spark Structured Streaming**, and prints alerts.

## Architecture
- **Kafka** (via Docker Compose) — topic `iot-events`
- **Producer** (`producer.py`) — sends IoT-like JSON messages
- **Spark** (`spark_app.py`) — consumes from Kafka, flags high temperature events

> Optional extension: write the output to **Parquet** (local or S3/MinIO) and wire metrics into **Prometheus/Grafana**.

## Prereqs
- Docker & Docker Compose
- Python 3.10+
- Java 8+ (for Spark)
- `pip install -r requirements.txt` for the producer

## Run

### 1) Start Kafka
```bash
docker-compose up -d
```

### 2) Produce messages
```bash
pip install -r requirements.txt
python producer.py --bootstrap localhost:9092 --topic iot-events --rate 5
```

### 3) Start Spark streaming consumer
Make sure Spark is installed and add the Kafka package on submit:
```bash
spark-submit \
  --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.5.0 \
  spark_app.py
```

You should see alerts streaming in the console.

## Persist to Parquet (optional)
Replace the console sink with:
```python
alerts.writeStream.format("parquet") \
  .option("path", "data/out/alerts") \
  .option("checkpointLocation", "data/checkpoints/alerts") \
  .outputMode("append").start()
```

## Grafana/Prometheus (optional)
- Expose Spark metrics via Dropwizard / Prometheus JMX exporter.
- Scrape and visualize processing rates, input rows per second, and batch durations.

## Cleanup
```bash
docker-compose down -v
```