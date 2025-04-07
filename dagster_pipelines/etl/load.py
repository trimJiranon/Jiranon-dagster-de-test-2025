from dagster import get_dagster_logger
import duckdb
import pandas as pd
import os

logger = get_dagster_logger()

def load_to_duckdb(df: pd.DataFrame, table_name: str) -> None:
    try:
        db_path = os.getenv("DUCKDB_PATH", "/tmp/plan.db")
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        with duckdb.connect(db_path) as con:
            logger.info("Connected to DuckDB successfully.")
            
            con.sql("CREATE SCHEMA IF NOT EXISTS plan;")
            con.register('df_view', df)
            
            con.sql(f"CREATE OR REPLACE TABLE plan.plan.{table_name} AS SELECT * FROM df_view;")
            result = con.sql(f"SELECT * FROM plan.plan.{table_name} LIMIT 1").fetchone()
            logger.info(f"Sample record from {table_name}: {result}")
            logger.info(f"Data successfully inserted into table '{table_name}'.")
    except Exception as e:
        logger.error(f"Error loading data into DuckDB: {e}")
        raise