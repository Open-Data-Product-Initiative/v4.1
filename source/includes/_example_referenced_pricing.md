# Referenced Pricing Pattern

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
    
  pricingPlans:
    en:
      - name: Basic Access
        price: 0.00
        unit: recurring
        billingDuration: month
        offering:
          - 10,000 API calls/month
        serviceLevel:
          $ref: "#/components/slaSets/0"
        dataQuality:
          $ref: "#/components/dataQualities/0"
        interface:
          $ref: "#/components/interfaces/0"
        paymentGateway:
          $ref: "#/components/paymentGateways/0"

      - name: Premium Access
        price: 500.00
        unit: recurring
        billingDuration: month
        offering:
          - 100,000 API calls/month
          - AI agent access
        serviceLevel:
          $ref: "#/components/slaSets/1"
        dataQuality:
          $ref: "#/components/dataQualities/1"
        interface:
          $ref: "#/components/interfaces/1"
        paymentGateway:
          $ref: "#/components/paymentGateways/1"
```
