from src.api_to_s3 import fetch_census_data, upload_to_s3
import src.s3_helper as s3
import src.duckdb_helper as d
from utils.logger import logger
from dotenv import load_dotenv
import os

load_dotenv()

SCHEMA = os.getenv("RAW_SCHEMA")
BUCKET = os.getenv("S3_BUCKET_NAME")
OBJECT_PATH = os.getenv("RAW_OBJECT_PATH")


def main():
## Census API
    logger.info("Starting Census data pipeline")
    api_key = os.getenv("CENSUS_API_KEY")

    census_data = fetch_census_data(api_key)
    upload_to_s3(census_data, "api", "census_acs5_2022.csv")
    logger.info("Pipeline complete")

    d.convert_to_duckdb(SCHEMA, "census_api", census_data, logger)

# NPPES

    d.s3_to_duckdb(SCHEMA, "nppes_raw", BUCKET, f"{OBJECT_PATH}nppes/npidata_pfile_20050523-20250413.csv", logger)

## States

    d.s3_to_duckdb(SCHEMA, "states_raw", BUCKET, f"{OBJECT_PATH}geographic/ssa_fips_state_county_2025.csv", logger)

## Taxonomy

    d.s3_to_duckdb(SCHEMA, "taxonomy_raw", BUCKET, f"{OBJECT_PATH}geographic/nucc_taxonomy_250.csv", logger)

## Zip_county

    zip_county_raw = s3.get_raw_excel_data_from_AWS(BUCKET, f"{OBJECT_PATH}geographic/ZIP_COUNTY_032025.xlsx", logger)

    d.convert_to_duckdb(SCHEMA, "zip_county_raw", zip_county_raw, logger)

if __name__ == "__main__":
    main()
