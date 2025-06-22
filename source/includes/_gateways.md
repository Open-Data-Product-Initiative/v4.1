# Payment Gateways

Payment Gateways **OBJECT** describes the methods to define payment gateways for pricing plans as references

## Optional attributes and elements

> Example of Payment Gateways object usage:

```yml

paymentGateways:
  - name: Agent
    description:
      en: Payment gateway for AI agents
    type: Axio
    version: 1
    reference: 'https://www.x402.org/'
    spec: |
      paymentMiddleware("0xYourAddress", {"/your-endpoint": "$0.01"});
  - name: API
    description:
      en: API consumption Payment gateway for humans
    type: Stripe
    version: 1
    reference: 'https://docs.stripe.com/'
    spec: |
      link or code to ignite purchase

```

| <div style="width:150px">Element name</div>   | Type  | Options  | Description  |
|---|---|---|---|
| **object** | type | Options | Desc |
