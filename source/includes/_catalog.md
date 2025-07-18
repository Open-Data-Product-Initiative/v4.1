# Data Product Catalog

> Example of catalog object usage:

```yml



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
| **products**                                | array  | -           | List of logical data products in the catalog |
| **productId**                               | string | -           | Unique ID for the logical data product (shared across variants) |
| **name**                                    | string | -           | Human-readable name of the product                              |
| **orgName**                                 | string | -           | Full name of the publishing organization                      |
| **orgId**                                   | string | -           | Unique identifier of the organization (e.g., domain-style ID) |



## Optional attributes and elements

| <div style="width:150px">Element name</div> | Type             | Options  | Description                                             |
| ------------------------------------------- | ---------------- | -------- | ------------------------------------------------------- |
| **title**                                   | string           | -        | Title of the catalog for display purposes               |
| **description**                             | string           | -        | Description of the catalog's purpose or content         |
| **generated**                               | string (date)    | ISO 8601 | Timestamp or date when the catalog was generated        |
| **publisher**                               | object           | -        | Metadata about the organization maintaining the catalog |
| **url**                                     | string (URI)     | -        | Website of the organization maintaining the catalog     |
| **tags**                                    | array of strings | -        | Keywords or themes associated with the logical product  |
| **description**                             | string           | -        | Human-readable explanation of the data product          |
| **categories**                              | string           | e.g., `transport`, `environment` | A thematic category for filtering/grouping |
| **created**                                 | string (date)    | ISO 8601 | Timestamp or date when the product was generated        |
| **updated**                                 | string (date)    | ISO 8601 | Timestamp or date when the product was last updated     |

 


Bring your ideas, questions, and use cases — [join the ODPS Discord](https://discord.gg/7KfnFxAc) and get involved!