# Inline Pattern

Use the named ODPS objects directly under `product` when a data product carries its own service, quality,
and access definitions. Reuse a named definition elsewhere in the same document with its JSON Pointer.

```yml
schema: https://opendataproducts.org/v4.1/schema/odps.yaml
version: '4.1'
product:
  details:
    en:
      name: Pets of the year
      productID: pets-of-the-year
      valueProposition: Reusable pet preference data for petstore services.
      description: An inline ODPS 4.1 example.
      visibility: private
      status: draft
      productVersion: '0.1.0'
      type: dataset

  SLA:
    declarative:
      default:
        dimensions:
          - dimension: uptime
            objective: 99
            unit: percent

  dataQuality:
    declarative:
      default:
        dimensions:
          - dimension: completeness
            objective: 95
            unit: percentage
    executable:
      - dimension: completeness
        type: Custom
        spec:
          rule: pet_id_must_be_present

  dataAccess:
    API:
      outputPortType: API
      format: JSON
      authenticationMethod: OAuth
      specification: OAS
      specsURL: https://example.org/pets/openapi.yaml
      accessURL: https://api.example.org/pets
      documentationURL: https://example.org/pets/docs
```
