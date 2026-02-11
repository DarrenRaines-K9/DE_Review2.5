select code,
       grouping,
       classification,
       specialization
from {{ source('nppes_raw', 'taxonomy_raw') }}