select
    p.state,
    p.county_fips as county,
    t.classification,
    count(distinct p.npi) as provider_count
from {{ ref('provider_directory') }} p
left join {{ ref('stg_taxonomy_data') }} t
  on p.taxonomy_code = t.code
group by 
    p.state,
    p.county_fips,
    t.classification
