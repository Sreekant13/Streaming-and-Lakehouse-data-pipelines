# Data Lakehouse (Local Simulation)

Lakehouse-style batch analytics using **Parquet + DuckDB** locally (simulating S3 + Glue + Athena without cloud cost).

## Zones
- `data/raw` — drop raw CSV here (e.g., NYC Taxi data).
- `data/processed` — PySpark writes cleaned Parquet.

## Run
1) Put a sample CSV in `data/raw/nyc_taxi.csv`  
   - Try a small subset or any public CSV with columns like `fare_amount`, `tip_amount`, `passenger_count`.

2) Run ETL (simulating Glue)
```bash
spark-submit etl_spark.py
```

3) Run Analytics (simulating Athena/Spectrum)
```bash
pip install duckdb
python duckdb_analytics.py
```

You should see aggregated results printed to the console.

## dbt Placeholder
Use `dbt/` to define SQL models (staging/curated) if desired.
- For a local dev flow, use **dbt-duckdb** adapter to run transformations against Parquet.

## Suggested Extensions
- Replace local paths with S3 URIs and use Glue Catalog
- Add partitioning by date
- Schedule with cron/Airflow
- Visualize with Tableau or Apache Superset