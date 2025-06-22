# Mandatory-only example

Example data product with just the mandatory elements and attributes. This is the minimal representation of a data product metadata that is expected to be found from every data product following ODPS standard. This bare minimum can be expanded with other elements and attributes defined in the specification. Also the possibilty to use extensions exists if local additions are needed. 

> Example of mandatory-only elements and attributes Open Data Product specification instance:

```yml

schema: https://opendataproducts.org/v3.0rc/schema/odps.yaml
version: 3.0
product:
  en:
    name: Pets of the year
    productID: 123456are
    visibility: private
    status: draft
    type: derived data

```
