# Components

Components object contains reusable objects to be used in various parts of the spec for example in Pricing. In the Pricing you might have 3 pricing plans and each can have different level of SLAs and Data Quality or Access. As an example. We have a data product which is for human and AI agent consumers. Obviously the access is different for both. Humans use API access and AI Agent uses MCP server (reusing the API perhaps). 

More over, the pricing might have Freemium and Premium plans as tiers. Then the SLA levels and/or Data Quality might differ. DAta Product provider wants to set different SLAs to both tiers. But in this case they want to set the sam Data Quality (reuse setting).

On the right is components needed to fulfill the above need and use case. 

## Standard Components

ODPS contains Standardized Components to use. Those cover most likely 80 percent of the use cases, but if not you can extend it with *x-* logic as usual. 

- SLAs
- Data Quality
- Interfaces
- PaymentGateways

> Example of License Object usage:


```yml 

Components:
    SLAs:
        Basic:
        - dimension: uptime
            displaytitle:
            - en: Uptime
            objective: 90
            unit: percent
        - dimension: responseTime
            objective: 500
            unit: milliseconds
        - dimension: updateFrequency
            objective: 1
            unit: days
        Extended:
        - dimension: uptime
            displaytitle:
            - en: Uptime
            objective: 99
            unit: percent
        - dimension: responseTime
            objective: 200
            unit: milliseconds
        - dimension: updateFrequency
            objective: 1
            unit: days

    Interfaces:
        API:
            description: REST API for real-time event data access.
            authenticationMethod: OAuth
            specification: OAS 3.0
            format: REST
            specsURL: urbanpulse.ai/urbanpulse.json
            documentationURL: urbanpulse.ai/docs 
        Agent:
            description: MCP interface for structured data access and agent interaction.
            authenticationMethod: Token
            specification: MCP 2025-03-26
            format: MCP
            specsURL: urbanpulse.ai/llms.txt
            documentationURL: urbanpulse.ai/llms-full.txt
    PaymentGateways:
        Agent:
            type: Axio
            version: 1.0
            reference: https://www.x402.org/
            spec: |
                paymentMiddleware("0xYourAddress", {"/your-endpoint": "$0.01"});
        API:
            type: Stripe
            version: 1.0
            reference: https://docs.stripe.com/
            spec: |
                links to ignite purchase

    DataQualities:
        Basic:
        - dimension: accuracy
            objective: 98
            unit: percentage
        - dimension: completeness
            objective: 90
            unit: percentage
   

  
```

## SLAs

| <div style="width:150px">Element name</div>   | Type  | Options  | Description  |
|---|---|---|---|
| **object** | type | Options | Desc |


## Data Quality

| <div style="width:150px">Element name</div>   | Type  | Options  | Description  |
|---|---|---|---|
| **object** | type | Options | Desc |

## Interfaces

| <div style="width:150px">Element name</div>   | Type  | Options  | Description  |
|---|---|---|---|
| **object** | type | Options | Desc |

## PaymentGateways

| <div style="width:150px">Element name</div>   | Type  | Options  | Description  |
|---|---|---|---|
| **object** | type | Options | Desc |