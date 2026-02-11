import os 
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import responses
from src.api_to_s3 import fetch_census_data

@responses.activate
def test_fetch_census_data():
    responses.add(
        responses.GET,
        "https://api.census.gov/data/2024/acs/acs5",
        json=[
            ["NAME", "B01003_001E", "B19013_001E", "B17001_002E", "state", "county"],
            ["Test County", "100", "50000", "10", "01", "001"]
        ],
        status=200
    )

    df = fetch_census_data(api_key="a1a4c38b286141cfaa74c4c37eae644768a3213a")

    assert df.height == 1
