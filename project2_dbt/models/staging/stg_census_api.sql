select
    split_part (name,',',1) as county,
    split_part (name,',',2) as state,
    population,
    median_income,
    poverty_count,
    county_fips,
    state_fips
from {{ source('nppes_raw', 'census_api') }}