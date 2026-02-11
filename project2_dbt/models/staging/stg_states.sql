select
fipscounty,
countyname_fips as county,
state_name
from {{ source('nppes_raw', 'states_raw') }}