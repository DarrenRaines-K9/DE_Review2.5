# DE_Review2.5

Second Data Engineering Assessment

## ⚡ Important: Learning Approach

This project emphasizes learning how to learn:

- Tool evaluation — You decide when to use Pandas vs Polars based on your research
- Documentation first — Read the docs, try it, break it, fix it
- Architecture decisions — Partitioning strategy, schema design, and optimization are your choices to justify
- Ask the right questions — Know when to research independently vs when to ask for help

## 📚 Business Scenario

**Client**: HealthAnalytics Platform

HealthAnalytics is building a national healthcare intelligence platform requiring:

## Business Challenge:

- Massive healthcare datasets (10GB+ provider files) requiring efficient processing
- Geographic intelligence integrating provider data with demographic and census information
- Data quality assurance for regulatory compliance and business intelligence accuracy
- Scalable architecture supporting weekly data updates and growing dataset volumes

## Technical Requirements:

- Process National Plan and Provider Enumeration System (NPPES) data (10GB+ CSV)
- Integrate geographic reference data and Census API information
- Build medallion architecture (raw → staging → marts) using dbt and DuckDB
- Stage raw data in S3 with intelligent organization
- Implement comprehensive dbt tests for data quality validation
- Demonstrate scalability patterns for 10x data volume growth

## 📊 Data Sources

**Primary Dataset: NPPES Healthcare Provider Data**

- Size: 10GB+ CSV file with provider information
- Complexity: Nested data structures, quality issues, regulatory requirements
- Update Pattern: Weekly updates requiring incremental processing
- Scale Challenge: Memory-efficient processing without infrastructure limitations

**Supporting Data Sources:**

- Geographic Crosswalk: ZIP-to-county mapping (Excel format)
- Census Demographics: Population and socioeconomic data via API
- Reference Data: FIPS codes, state mappings, healthcare taxonomy

## 📅 Project Timeline & Phases

Architecture & Foundation
**Architecture Design**

- Research and document your processing strategy (Pandas vs Polars — justify your choice)
- Design S3 organization for raw data staging
- Plan dbt project structure for medallion architecture
- Design DuckDB schema for analytical workloads

## Foundation Implementation

- Set up S3 bucket organization and upload raw data
- Initialize dbt project with DuckDB adapter
- Implement memory-efficient data loading (chunked processing)
- Validate architecture with sample data subset

## Core Pipeline Development

**Ingestion & Raw Layer**

- Full dataset processing with memory-efficient techniques
- S3 integration for raw data access
- dbt sources configuration pointing to S3/external files
- Error handling for data quality issues in source data

**Staging Layer**

1:1 cleaning models (Python or SQL — your choice per model)
Data type standardization and null handling
Geographic data integration
Census API data processing

## Analytics & Testing

**Marts Layer**

- Analytical models joining provider, geographic, and demographic data
- Business intelligence aggregations
- Performance optimization for complex queries

## dbt Tests (Required)

- Generic tests on all marts models (unique, not_null, accepted_values)
- Relationship tests validating referential integrity
- Custom singular tests for business logic validation
- Document your test coverage and rationale

## 💡 Marts Layer Guidance

Your marts layer should answer business questions by joining your cleaned staging models. Here are some directions to consider:

## Core Marts (Expected)

| Model                  | Description                                         | Likely Joins                   |
| ---------------------- | --------------------------------------------------- | ------------------------------ |
| provider_directory     | Enriched provider records with location context     | provider + geographic          |
| providers_by_geography | Provider counts aggregated by state, county, or ZIP | provider + geographic          |
| specialty_distribution | What specialties exist in which regions             | provider + geographic          |
| provider_density       | Providers per capita by geographic area             | provider + geographic + census |

### Stretch Marts (If Time Allows)

| Model             | Description                                    |
| ----------------- | ---------------------------------------------- |
| underserved_areas | Regions with low provider-to-population ratios |
| specialty_gaps    | Geographic areas missing key specialties       |

## What We're Looking For

- Joins across staging models — Your marts should combine data, not just pass it through
- Business logic — Aggregations, calculations, or filters that answer real questions
- Tested outputs — Every mart should have dbt tests validating data quality
- Questions Your Marts Should Answer
- How many providers are in each state/county?
- Which areas have the most/least providers per capita?
- What is the specialty mix in a given region?
- Where might there be gaps in healthcare coverage?

Design your marts to answer questions a healthcare analyst would actually ask.
Production Readiness

## Quality Assurance

- Full pipeline run with complete dataset
- Test execution and failure resolution
- Performance profiling and optimization
- dbt docs generation
