

SELECT ZIP as zip_code,
       COUNTY as county_fips,
       USPS_ZIP_PREF_CITY as city,
       USPS_ZIP_PREF_STATE as state,
       RES_RATIO as residential_ratio,
       BUS_RATIO as business_ratio,
       OTH_RATIO as other_ratio,
       TOT_RATIO as total_ratio
from {{ source('nppes_raw', 'zip_county_raw') }}
