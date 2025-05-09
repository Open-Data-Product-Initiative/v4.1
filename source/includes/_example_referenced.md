# Referenced Pattern

The objects are not defined inline, but instead references a reusable definition in the components section using a $ref path.

> Example:

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
    
  serviceLevel:
    $ref: "#/components/slaSets/1"

  access:
    $ref: "#/components/interfaces/0"

  dataQuality:
    $ref: "#/components/dataQualities/0"

  paymentGateway:
    $ref: "#/components/paymentGateways/1"
```
