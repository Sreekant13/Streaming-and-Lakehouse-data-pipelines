# data_lakehouse/duckdb_analytics.py
# Query Parquet (processed zone) using DuckDB, simulating Athena/Spectrum queries.

import duckdb

PARQUET_GLOB = "data/processed/nyc_taxi_parquet/*.parquet"

con = duckdb.connect(database=":memory:")
con.execute(f"""
    CREATE TABLE trips AS
    SELECT * FROM parquet_scan('{PARQUET_GLOB}');
""")

# Example analytics
result = con.execute("""
    SELECT passenger_count, ROUND(AVG(fare_amount), 2) AS avg_fare
    FROM trips
    GROUP BY passenger_count
    ORDER BY passenger_count
""").fetchall()

print("Avg fare by passenger_count:")
for row in result:
    print(row)