import io
import sys
import os 
import boto3
import polars as pl
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from moto import mock_s3
from src.s3_helper import get_raw_excel_data_from_AWS



@mock_s3
def test_get_raw_excel_data_from_AWS(mocker):
    # Patch boto3.Session to not require AWS profile
    mocker.patch("boto3.Session", return_value=boto3.Session())

    # Setup fake S3
    s3 = boto3.client("s3", region_name="us-east-1")
    s3.create_bucket(Bucket="test-bucket")

    # Prepare a sample Excel file
    data = pl.DataFrame({"id": [1, 2], "value": ["a", "b"]})
    buffer = io.BytesIO()
    data.write_excel(buffer)
    buffer.seek(0)
    s3.put_object(Bucket="test-bucket", Key="sample.xlsx", Body=buffer.getvalue())

    # Call the function under test
    fake_logger = mocker.Mock()
    result = get_raw_excel_data_from_AWS("test-bucket", "sample.xlsx", fake_logger)

    # Check it worked
    assert not result.is_empty()
