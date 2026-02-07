import io
import os
import requests
import polars as pl
import boto3
from dotenv import load_dotenv
from utils.logger import logger



load_dotenv()


def fetch_census_data(api_key, year=2024):
    """Fetch Census ACS 5-Year county-level demographic data and return a Polars DataFrame."""
    logger.info(f"Fetching Census data for year {year}")

    url = f"https://api.census.gov/data/{year}/acs/acs5"
    params = {
        "get": "NAME,B01003_001E,B19013_001E,B17001_002E",
        "for": "county:*",
        "in": "state:*",
        "key": api_key,
    }

    response = requests.get(url, params=params)
    response.raise_for_status()
    raw_census_response = response.json()

    column_headers = [
        "name",
        "population",
        "median_income",
        "poverty_count",
        "state_fips",
        "county_fips",
    ]
    census_data = pl.DataFrame(
        raw_census_response[1:], schema=column_headers, orient="row"
    )

    census_data = census_data.with_columns(
        [
            pl.col("population").cast(pl.Int64, strict=False),
            pl.col("median_income").cast(pl.Int64, strict=False),
            pl.col("poverty_count").cast(pl.Int64, strict=False),
        ]
    )
    print(census_data.head())
    logger.info(f"Fetched {len(census_data)} counties")
    return census_data


def upload_to_s3(census_data, folder, filename):
    """Write a Polars DataFrame to CSV in memory and upload to S3."""
    bucket = os.getenv("S3_BUCKET_NAME")
    prefix = os.getenv("S3_FOLDER_PREFIX")
    profile = os.getenv("AWS_NAME")

    s3_key = f"{prefix}/raw/{folder}/{filename}"

    csv_buffer = io.BytesIO()
    census_data.write_csv(csv_buffer)
    csv_buffer.seek(0)

    session = boto3.Session(profile_name=profile)
    s3_client = session.client("s3")
    s3_client.upload_fileobj(csv_buffer, bucket, s3_key)

    logger.info(f"Uploaded to s3://{bucket}/{s3_key}")
