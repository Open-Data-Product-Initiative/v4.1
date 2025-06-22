# Payment Gateways

Payment Gateways **OBJECT** describes the methods to define payment gateways for pricing plans as references

## Optional attributes and elements

> Example of Payment Gateways object usage:

```yml

paymentGateways:
  - id: Agent
    description:
      en: Payment gateway for AI agents
    type: Axio
    version: 1
    reference: 'https://www.x402.org/'
    spec: |
      paymentMiddleware("0xYourAddress", {"/your-endpoint": "$0.01"});

  - id: API
    description:
      en: API consumption payment gateway for humans
    type: Stripe
    version: 1
    reference: 'https://docs.stripe.com/'
    spec: |
      // Replace this with your actual implementation or link
      stripe.createCheckoutSession({
        amount: 100, // in cents
        currency: 'usd',
        success_url: 'https://your-platform.com/success',
        cancel_url: 'https://your-platform.com/cancel'
      });

```

| <div style="width:150px">Element name</div>   | Type  | Options  | Description  |
|---|---|---|---|
| **object** | type | Options | Desc |
