select
    NPI,
    "Entity Type Code" as Entity_Type,
    "Provider Organization Name (Legal Business Name)" as Provider_Org_name,
    case when  "Provider Organization Name (Legal Business Name)" is not null then 'Organization'
         else 'Individual'
             end as provider_type,
    "Provider Last Name (Legal Name)" as Provider_Last_Name,
    "Provider First Name" as Provider_First_Name,
    "Provider Sex Code" as Provider_Gender_Code,
    "Certification Date" as Certificate_Date,
    "Last Update Date" as Last_Update_Date,
    "Provider First Line Business Practice Location Address" as Provider_Address_1,
    "Provider Business Practice Location Address City Name" as Provider_City_Name,
    "Provider Business Practice Location Address State Name" as Provider_State_Name,
    rtrim(substr("Provider Business Practice Location Address Postal Code",1,5)) as Provider_Postal_Code,
    "Provider Business Practice Location Address Country Code (If outside U.S.)" as Provider_Country_Code,
    "Provider Business Practice Location Address Telephone Number" as Provider_Telephone_Number,
    "Healthcare Provider Taxonomy Code_1" as Provider_Taxonomy_Code_1
    
from {{ source('nppes_raw', 'nppes_raw') }}
where
  "Provider Organization Name (Legal Business Name)" is not null
  or "Provider First Name" is not null
  or "Provider Last Name (Legal Name)" is not null