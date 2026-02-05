from src.api_to_s3 import fetch_census_data, upload_to_s3
from utils.logger import logger
from dotenv import load_dotenv
import os

load_dotenv()


def main():
    logger.info("Starting Census data pipeline")
    api_key = os.getenv("CENSUS_API_KEY")

    census_data = fetch_census_data(api_key)
    upload_to_s3(census_data, "api", "census_acs5_2022.csv")
    logger.info("Pipeline complete")


if __name__ == "__main__":
    main()
