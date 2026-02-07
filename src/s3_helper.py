import os
import boto3
import io
import polars as pl
from dotenv import load_dotenv

load_dotenv()

SSO_PROFILE_NAME = os.getenv("AWS_NAME")
SSO_REGION_NAME = os.getenv("AWS_REGION")

    
def get_raw_excel_data_from_AWS(bucket_name, object_key, logger) -> pl.DataFrame | None:
    try:
        s3_path = f"s3://{bucket_name}/{object_key}"
        logger.info(f"Scanning {s3_path}")

        session = boto3.Session(profile_name=SSO_PROFILE_NAME)
        s3_client = session.client('s3')

        response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
        excel_data = pl.read_excel(io.BytesIO(response['Body'].read()))

        logger.info(
            f'Loaded {object_key} into DataFrame '
            f'({excel_data.height} rows, {excel_data.width} columns)'
        )

        return excel_data

    except Exception as e:
        logger.error(
            f"Failed to scan s3://{bucket_name}/{object_key}: {e}",
            exc_info=True
        )
        raise