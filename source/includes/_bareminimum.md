# Mandatory-only example

Example data product with just the mandatory elements and attributes. This is the minimal representation of a data product metadata that is expected to be found from every data product following ODPS standard. This bare minimum can be expanded with other elements and attributes defined in the specification. Also the possibilty to use extensions exists if local additions are needed. 

> Example of mandatory-only elements and attributes Open Data Product specification instance:

```yml

schema: https://raw.githubusercontent.com/Open-Data-Product-Initiative/open-data-product-spec-dev/ddbc069196a664d0e28a0f3dc7c1c7fb49b64591/source/schema/odps-dev-json-schema.json
version: dev
product:
  en:
    name: Pets of the year
    productID: 123456are
    visibility: private
    status: draft
    type: derived data
  pricingPlans:
    en:
    - name: Freemium Package
      priceCurrency: EUR
      price: '0.00'
      billingDuration: month
      unit: recurring
      maxTransactionQuantity: 1000
      offering:
        - item 1

```
