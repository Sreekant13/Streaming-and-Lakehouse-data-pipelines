# Data Engineering Portfolio

Two production-style, minimal projects you can demo quickly and talk through in interviews.

## Projects
1. **streaming_pipeline** — Real-time analytics with Kafka + Spark Structured Streaming (local dev via Docker).
2. **data_lakehouse** — Lakehouse-style batch analytics using Parquet + DuckDB (Glue/Athena simulated locally), with a dbt placeholder.

Each project is self-contained with a `README.md` outlining setup and run instructions.

> Tip: After verifying locally, create a GitHub repo (e.g., `data-engineering-portfolio`) and push this tree.
> You can then link to each project from your resume.

## Quickstart
```bash
# clone and enter
git clone <your-repo-url>
cd data-engineering-portfolio

# choose a project
cd streaming_pipeline
# see README for commands

cd ../data_lakehouse
# see README for commands
```

---

## Tech Stack Coverage
- **Streaming:** Apache Kafka, Spark Structured Streaming
- **Batch:** PySpark-style transforms, Parquet
- **Query Layer:** DuckDB (simulating Athena/Spectrum locally)
- **Infra:** Docker Compose for Kafka/ZooKeeper locally
- **Observability:** Notes for wiring into Grafana/Prometheus (optional extension)
- **Orchestration (optional):** dbt placeholder included for transforming curated models