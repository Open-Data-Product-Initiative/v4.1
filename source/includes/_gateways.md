# Payment Gateways

Payment Gateways **OBJECT** describes the methods to define payment gateways for pricing plans as references

## Optional attributes and elements

> Example of Payment Gateways object usage:

```yml

paymentGateways:
  default:
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

  Agent:
    description:
      en: Payment gateway for AI agents
    type: Axio
    version: 1
    reference: 'https://www.x402.org/'
    spec: |
      paymentMiddleware("0xYourAddress", {"/your-endpoint": "$0.01"});

  

```

| <div style="width:150px">Element name</div>   | Type  | Options  | Description  |
|---|---|---|---|
| **paymentGateways** | object | - | Object containing all defined payment gateway configurations. Each key is a named reference (e.g. `default`, `agent`) that can be reused in pricing plans. |
| **default** | object | - | Named default payment gateway used. If you use paymentGateways object, this default is expected to be first option and is defined always. Can be referenced using `$ref: '#/paymentGateways/default'`. <br/> <br/> In the example, _agent_ payment gateway as an example of freely named gateway which can be referenced using `$ref: '#/paymentGateways/agent'`. You can follow the same pattern and create more |
| **description** | object | string [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) | Multilingual descriptions of the payment gateway. Enables UI rendering in multiple languages. |
| **type** | string | Stripe, Axio, Checkout, Custom | Defines the payment system or protocol used. Use predefined values. `Custom` allows custom or internal solutions. |
| **version** | string | Free-form version label | Indicates the version of the payment gateway specification, SDK, or integration logic. |
| **reference** | URL | Valid URL | Points to documentation or developer reference for the payment gateway system. |
| **spec** | string / YAML / URL | - | Contains the executable or declarative logic for the payment gateway integration. Can be inline YAML, stringified logic, or link to external file. |
