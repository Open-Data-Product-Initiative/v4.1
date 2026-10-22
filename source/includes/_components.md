# Reusable Components

ODPS 4.1 keeps reusable service, quality, access, and payment definitions inside `product`. There is no
top-level `Components` object and no index-based component reference. A publisher gives each reusable
definition a stable name and references it with a JSON Pointer.

## SLA profiles

```yml
SLA:
  declarative:
    default:
      name:
        en: Standard service
      dimensions:
        - dimension: uptime
          objective: 99
          unit: percent
```

Reference the profile with `$ref: '#/product/SLA/declarative/default'`.

## Data quality profiles

```yml
dataQuality:
  declarative:
    default:
      displaytitle:
        en: Standard data quality
      dimensions:
        - dimension: accuracy
          objective: 98
          unit: percentage
```

Reference the profile with `$ref: '#/product/dataQuality/declarative/default'`.

## Data access definitions

```yml
dataAccess:
  API:
    name:
      en: Events API
    description:
      en: Authenticated API access to current events.
    outputPortType: API
    format: JSON
    authenticationMethod: OAuth
    specification: OAS
    specsURL: https://example.org/openapi.yaml
    accessURL: https://api.example.org/events
    documentationURL: https://example.org/docs/events-api
```

Reference the access method with `$ref: '#/product/dataAccess/API'`.

## Payment gateway definitions

```yml
paymentGateways:
  API:
    description:
      en: API payment gateway
    type: Stripe
    version: '1'
    reference: https://docs.stripe.com/
    spec:
      action: createCheckoutSession
```

Reference the payment gateway with `$ref: '#/product/paymentGateways/API'`.
