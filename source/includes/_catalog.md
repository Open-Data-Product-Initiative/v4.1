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
    unit: triel
    priceCurrency: EUR
    price: 0.00

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
| **priceCurrency** | string  |  Use standard formats: [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217) currency format e.g. "USD"; Ticker symbol for cryptocurrencies e.g. "BTC"  |  The primary currency used in pricing. Platforms are assumed to use this as primary currency if currency conversions are used to display product pricing in different locations for various currencies. If the *unit* is revenue-sharing, then this attribute value MUST be percentage.  |
| **price** | string  | -  | The offer price of a product, or of a price component, or revenue-sharing percentage. <br/><br/> If the *unit* of pricing is revenue-sharing, then this *price* attribute value is percentage value. <br/><br/> Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator. Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similiar Unicode symbols. <br/><br/>With *data-volume* the price is for each 1GB of data. |
| **billingDuration** | string  | options: instant, day, week, month, year  | Specifies for how long this price (or price component) will be billed. Can be used, for example, to model the contractual duration of a subscription or payment plan.  |
| **unit** | string | One of: One-time-payment, Pay-per-use, Recurring, Revenue-sharing, Data-volume , Pay-what-you-want, Freemium, Open-data, Value-based, On-request, Trial | One-time-payment is for single time purchase purposes, further purchaces are not intended to continue under same agreement. <br/><br/> *Pay-per-use* is intended for continuous usage and price set is for each successful usage action. <br/><br/> *Recurrring* is intended for continuous time period plans. <br/><br/>*Revenue sharing* is a performance-based income model. An effective revenue sharing deal structure is offering your expertise to a business owner to help them grow their business. In return, you get paid a percentage of the revenue as a royalty fee. <br/><br/> *Freemium* is for free access. Use this option also for open data. <br/><br/> *Data-volume* is for data amount based pricing in which customer pays based on the served data amount. The price is always for 1GB of data. <br/><br/> *Pay-what-you-want*  is a pricing system where buyers pay any desired amount for a given commodity, sometimes including zero. In some cases, a minimum (floor) price may be set, and/or a suggested price may be indicated as guidance for the buyer. The buyer can also select an amount higher than the standard price for the commodity. If the floor price is set, use *minPrice* attribute. <br/><br/> *Open-data*  is an explicit pricing plan category for open data. By default open data should be free, but in some cases it can have a price. <br/><br/> *Value-based* is value-based selling unit. Present the outcome of your story with solid data and a measurable impact with help of *offering* attribute. Example: “We can lower the energy bill in heating by $8-13/square meter in a year. Try out simulator to calculate your value!”. Use optional *valueSimulator* attribute to provide link (URL) to value simulator you have created. In order to set base fee for value-based plan, you can for example set monthly (*billingDuration*) plan with base see with help of *minPrice* attribute. <br/><br/> *On-request* is for plans in which customer is given access to data product after contacting provider. 


 


Bring your ideas, questions, and use cases — [join the ODPS Discord](https://discord.gg/7KfnFxAc) and get involved!