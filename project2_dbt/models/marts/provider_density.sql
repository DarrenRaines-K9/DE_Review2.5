with provider_counts as (

    select
        state,
        county_fips as county,
        count(distinct npi) as provider_count
    from {{ ref('provider_directory') }}
    group by state, county_fips
),
population as (

    select
        state,
        county_fips as county,
        population,
        poverty_count
    from {{ ref('stg_census_api') }}
)
select
    p.state,
    p.county,
    pop.population,
    pop.poverty_count,
    p.provider_count / nullif(pop.population, 0)::float as providers_per_capita
from provider_counts p
left join population pop
  on p.state = pop.state
 and p.county = pop.county
