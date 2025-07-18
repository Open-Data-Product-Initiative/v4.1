# Data Product Catalog

> Example of catalog object usage:

```yml
version: "1.0"
title: Abu Dhabi Smart City ODPS Catalog
description: >
  A curated list of ODPS-compliant data products 
  published by multiple Abu Dhabi government entities.
generated: 2025-07-18

publisher:
  orgName: Department of Government Enablement
  orgId: dge.abudhabi
  url: https://www.dge.abudhabi

products:
  - productId: air-quality-index
    name: Air Quality Index
    orgName: Environment Agency – Abu Dhabi
    orgId: ead.abudhabi
    url: https://data.ead.gov/odps/air-quality.yaml
    tags: ["environment", "pollution", "aqi"]
    description: Daily air quality readings from across Abu Dhabi emirate.
    categories: environment
    created: 2023-11-12
    updated: 2025-06-30

  - productId: traffic-accidents
    name: Traffic Accidents in Abu Dhabi
    orgName: Abu Dhabi Police
    orgId: police.abudhabi
    url: https://data.adpolice.gov/odps/traffic-accidents.yaml
    tags: ["traffic", "safety", "transport"]
    description: Historical and real-time traffic accident data across the city.
    categories: transport
    created: 2024-04-10
    updated: 2025-05-28

  - productId: water-consumption
    name: Water Consumption by District
    orgName: Abu Dhabi Distribution Company
    orgId: addc.abudhabi
    url: https://data.addc.abudhabi/odps/water-consumption.yaml
    tags: ["utilities", "consumption", "water"]
    description: Monthly water usage data across residential districts.
    categories: utilities
    created: 2023-07-01
    updated: 2025-04-15



```

Instead of changing ODPS (which defines individual products), we define a **sidecar schema** (e.g., odps-catalog.yaml) that:

* Acts as a manifest of ODPS product files
* Provides minimal metadata for grouping or navigation
* Is designed for Git-based use or portal ingestion

This follows the “composition over extension” principle.

### Outcome

This method:

* Keeps the ODPS spec focused and clean
* Enables Git-based catalogs and open collaboration
* Offers a bridge to DCAT (without enforcing RDF/OWL complexity)
* Aligns with ODPS-as-code values

### Example Automation Scenarios

* Validation script that checks all *.yaml files against the ODPS schema
* GitHub Action that regenerates a static HTML/JSON catalog from ODPS YAML files
* CI/CD job that publishes selected products to a data portal when main branch updates

### Use Case in Government or Enterprise

Imagine a Platform storing its official ODPS product definitions in a public GitHub repo. Each department can:

* Maintain their own odps/*.yaml files
* Submit them via pull request
* Have automatic validation before merging
* Allow public feedback via GitHub issues

It becomes a living catalog, governed like software.

## Mandatory attributes and elements


| <div style="width:150px">Element name</div> | Type   | Options     | Description                                  |
| ------------------------------------------- | ------ | ----------- | -------------------------------------------- |
| **version**                                 | string | e.g., `1.0` | Version of the catalog schema                |
| **title**                                   | string           | -        | Title of the catalog for display purposes               |
| **description**                             | string           | -        | Description of the catalog's purpose or content         |
| **orgName**                                 | string | -           | Full name of the data product publishing organization                      |
| **url**                                     | string (URI)     | -        | Website of the organization maintaining the catalog     |


## Optional attributes and elements

| <div style="width:150px">Element name</div> | Type             | Options  | Description                                             |
| ------------------------------------------- | ---------------- | -------- | ------------------------------------------------------- |
| **products**                                | array  | -           | List of logical data products in the catalog |
| **productId**                               | string | -           | Unique ID for the logical data product                        |
| **name**                                    | string | -           | Human-readable name of the product                              |
| **orgId**                                   | string | -           | Unique identifier of the organization (e.g., domain-style ID) |
| **generated**                               | string (date)    | ISO 8601 | Timestamp or date when the catalog was generated        |
| **publisher**                               | object           | -        | Metadata about the organization maintaining the catalog |
| **tags**                                    | array of strings | -        | Keywords or themes associated with the logical product  |
| **description**                             | string           | -        | Human-readable explanation of the data product          |
| **logo**                                    | string (URI)     | -        | URI to the product logo image                           |
| **categories**                              | string           | e.g., `transport`, `environment` | Thematic categories for filtering/grouping |
| **created**                                 | string (date)    | ISO 8601 | Timestamp or date when the product was generated        |
| **updated**                                 | string (date)    | ISO 8601 | Timestamp or date when the product was last updated     |
| **rating**                                  | string           | -        | Product rating, example 4/5 or 3.2/10. The latter number indicates maximum and first the aggregated rating     |


 


Bring your ideas, questions, and use cases — [join the ODPS Discord](https://discord.gg/7KfnFxAc) and get involved!