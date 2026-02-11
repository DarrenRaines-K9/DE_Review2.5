select *
from {{ ref('provider_density') }}
where providers_per_capita < 0
