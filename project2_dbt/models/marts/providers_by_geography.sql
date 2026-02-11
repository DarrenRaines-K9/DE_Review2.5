select
    state,
    county_fips as county,
    zip_code,
    count(distinct npi) as provider_count
from {{ ref('provider_directory') }}
group by state, county_fips, zip_code
