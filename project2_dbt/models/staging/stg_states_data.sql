select
fipscounty,
countyname_fips as county,
state_name as state
from {{ source('nppes_raw', 'states_raw') }}