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



## SLAs Component

> Example:


```yml 
Components:
  slaSets:
    - name: Basic
      description:
        - en: Default SLA for internal and non-paying users
      slas:
        - dimension: uptime
          displayTitle:
            en: Uptime
          objective: 90
          unit: percent
        - dimension: responseTime
          objective: 500
          unit: milliseconds
        - dimension: updateFrequency
          objective: 1
          unit: days

    - name: Extended
      description:
        - en: Premium SLA for external users or partners
      slas:
        - dimension: uptime
          displayTitle:
            en: Uptime
          objective: 99
          unit: percent
        - dimension: responseTime
          objective: 200
          unit: milliseconds
        - dimension: updateFrequency
          objective: 1
          unit: days
```

| <div style="width:150px">SLA Dimension</div>   | Description | 
|---|---|
| **latency** | minimal amount of time before getting any response. |
| **uptime** | Uptime is a measure of system reliability, expressed as the percentage of time a machine, typically a computer, has been working and available. See more https://uptime.is/. |
| **responseTime** | amount of time to process external request. |
| **errorRate** | Maximum tolerated errors in data, percentage. |
| **endOfSupport** | The date at which your product will not have support anymore. |
| **endOfLife** | The date at which your product will not be available anymore. No support, no access. |
| **updateFrequency** | how often data is updates. |
| **timeToDetect** | How fast can you detect a problem? |
| **timeToNotify** | Once you see a problem, how much time do you need to notify your users? |
| **timeToRepair** | How long do you need to fix the issue once it is detected? |
| **emailResponseTime** | How long do you need to respond to email support requests? |



## Data Quality Component

> Example:

```yml 
Components:
    DataQuality:
        Basic:
        - dimension: accuracy
            objective: 98
            unit: percentage
        - dimension: completeness
            objective: 90
            unit: percentage

```

| <div style="width:150px">Data Quality Dimension</div>   | Description | 
|---|---|
| **accuracy** | The measurement of the veracity of data to its authoritative source |
| **completeness** | Data is required to be populated with a value (aka not null, not nullable). Completeness checks if all necessary data attributes are present in the dataset. |
| **conformity** | Data content must align with required standards, syntax (format, type, range), or permissible domain values. Conformity assesses how closely data adheres to standards, whether internal, external, or industry-wide. |
| **consistency** | Data should retain consistent content across data stores. Consistency ensures that data values, formats, and definitions in one group match those in another group. |
| **coverage** | All records are contained in a data store or data source. Coverage relates to the extent and availability of data present but absent from a dataset. |
| **timeliness** | The data must represent current conditions; the data is available and can be used when needed.  |
| **validity** | Validity refers to the extent to which the data accurately and appropriately represents the real-world object or concept it is supposed to describe. |
| **uniqueness** | Uniqueness means each record and attribute should be one-of-a-kind, aiming for a single, unique data entry |



## Interfaces Component

> Example:

```yml 
Components:
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
```

| <div style="width:150px">Element name</div>   | Type  | Options  | Description  |
|---|---|---|---|
| **object** | type | Options | Desc |



## PaymentGateways Component

> Example:

```yml 
Components:
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

```

| <div style="width:150px">Element name</div>   | Type  | Options  | Description  |
|---|---|---|---|
| **object** | type | Options | Desc |

