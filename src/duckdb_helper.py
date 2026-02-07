import os
import duckdb
import boto3
from dotenv import load_dotenv

load_dotenv()

SSO_PROFILE_NAME = os.getenv("AWS_NAME")
SSO_REGION_NAME = os.getenv("AWS_REGION")

def s3_to_duckdb(schema, table_name, bucket_name, object_key, logger):
    conn = duckdb.connect('project2_dbt/dev.duckdb')


    session = boto3.Session(profile_name=SSO_PROFILE_NAME, region_name=SSO_REGION_NAME)
    credentials = session.get_credentials()
    access_key = credentials.access_key
    secret_key = credentials.secret_key
    token = credentials.token

    conn.execute(f"""
        SET s3_region='{SSO_REGION_NAME}';
        SET s3_access_key_id='{access_key}';
        SET s3_secret_access_key='{secret_key}';
    """)
    
    if token:
        conn.execute(f"SET s3_session_token='{token}';")

    s3_path = f"s3://{bucket_name}/{object_key}"
    logger.info(f"Ingesting {s3_path} into DuckDB")

    conn.execute(f"CREATE OR REPLACE TABLE {schema}.{table_name} AS SELECT * FROM read_csv_auto('{s3_path}', ignore_errors=true)")

    logger.info(f"DuckDB table {schema}.{table_name} created and/or updated")

    print(conn.execute(f"SHOW TABLES FROM {schema}").fetchall())

    conn.close()


def convert_to_duckdb(schema, table_name, data, logger):
    conn = duckdb.connect('project2_dbt/dev.duckdb')

    conn.execute(f"CREATE OR REPLACE TABLE {schema}.{table_name} AS SELECT * FROM data")

    logger.info(f"DuckDB table {schema}.{table_name} created and/or updated")

    print(conn.execute(f"SHOW TABLES FROM {schema}").fetchall())

    conn.close()