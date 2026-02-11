with providers as (

    select
        npi,
        provider_type,
        provider_last_name,
        provider_first_name,
        provider_org_name,
        provider_state_name as state,
        provider_city_name as city,
        provider_postal_code as zip_code,
        provider_taxonomy_code_1 as taxonomy_code
    from {{ ref('stg_nppes_data') }}
),
zip_geo as (

    select
        zip_code,
        county_fips,
        state,
        city
    from {{ ref('stg_zip_county') }}

)
select
    p.npi,
    p.provider_type,
    p.provider_last_name,
    p.provider_first_name,
    p.provider_org_name,
    p.state,
    z.county_fips,
    p.city,
    p.zip_code,
    p.taxonomy_code
from providers p
left join zip_geo z
  on p.zip_code = z.zip_code
