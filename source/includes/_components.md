# Components

Components object contains reusable objects to be used in various parts of the spec for example in Pricing. In the Pricing you might have 3 pricing plans and each can have different level of SLAs and Data Quality or Access. As an example. We have a data product which is for human and AI agent consumers. Obviously the access is different for both. Humans use API access and AI Agent uses MCP server (reusing the API perhaps). 

More over, the pricing might have Freemium and Premium plans as tiers. Then the SLA levels and/or Data Quality might differ. DAta Product provider wants to set different SLAs to both tiers. But in this case they want to set the sam Data Quality (reuse setting).

On the right is components needed to fulfill the above need and use case. 

## Optional attributes and elements

> Example of License Object usage:


```yml 

Components:
  SLAs:
    Basic:
      declarative:
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
      declarative:
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

  
```
| <div style="width:150px">Element name</div>   | Type  | Options  | Description  |
|---|---|---|---|
| **license** | element | - |  Binds the licensing related elements and attributes together. |
| **en** | attribute | [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) defined 2-letter codes | This element binds together other product attributes and expresses the langugage used. In the example this is "en", which indicates that product details are in English. If you would like to use Arabic details, then name the element "ar". The naming of this element follows options (language codes) listed in [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) standard. <br/><br/> You can have product details in multiple languages simply by adding similar sets like the example - just change the binding element name to matching language code. <br/><br/> The pattern to implement multilanguage support for data products was adopted from de facto UI translation practices. The attributes inside this element are commonly rendered in the UI for the consumer and providing a simple way to implement that was the driving reasoning. See for example  [JSON - Multi Language](https://simplelocalize.io/docs/file-formats/multi-language-json/) |
| **scope** | element | - |  Extent, range, coverage, area or space of the license. |
| **definition** | string | text content, max length 512 chars  | Background and purpose of the license. |
| **restrictions** | string | text content, max length 512 chars  | Restrictions of the license. |
| **geographicalArea** | string |  ISO 3166-1 alpha-2 codes | License right restricted to the geographical area. |
| **permanent** | boolean | true/false |  License with no expiration date. |
| **exclusive** | boolean | true/false |  The exclusive license holder is given complete control over the use of the data product, and no other person or organization is allowed to use it during the term of the license agreement. |
| **rights** | array |  Options: Reproduction <i>(rights to reproduce)</i>, Display <i>(disclose data to others)</i>, Distribution <i>(right to distribute)</i>, Adaptation <i>(right for derivate work)</i>, Reselling <i>(right to resell)</i>, Transferring <i>(transferable data license)</i>, Sublicensing <i>(license grant may include a right to sublicense)</i>| Rights granted by the licence. The texts in brackets and <i>italic</i> are intended to describe rights. |
| **termination** | element | - | Licence termination and continuity related conditions. |
| **noticePeriod** | integer | unit is days | The notice period is a particular time that an data product provider or consumer must give before ending the contract. This time window allows both sides to make the necessary preparations, guaranteeing an unhindered transfer. |
| **terminationConditions** | string | text content, max length 512 chars | Cancellation conditions of the license. |
| **continuityConditions** | string |  text content, max length 512 chars | Continuity conditions of the license. |
| **governance** | element | - | Governance is the approach taken to ensure that the agreed outcomes are being fulfilled. |
| **ownership** | string | text content, max length 512 chars | Data product licensing ownership. |
| **audit** | string | text content, max length 512 chars | License auditing terms. |
| **warranties** | string | text content, max length 512 chars | License warranties. |
| **damages** | string | text content, max length 512 chars | Damages refers to the sum of money (i.e. indemnifications) for a breach of some duty or violation of license right. |
| **confidentiality** | string | text content, max length 512 chars| Restrictions and requirements imposed on the Data User regarding e.g. the use and disclosure of the Data Holder's confidential information. |
| **applicableLaws** | string | text content, max length 512 chars | Applicable laws, i.e local acts, degrees or law. |
| **forceMajeure** | string | text content, max length 512 chars | Force majeure is a clause that is included in contracts to remove liability for unforeseeable and unavoidable catastrophes that interrupt the expected course of events and prevent participants from fulfilling obligations. These clauses generally cover both natural disasters and catastrophes created by humans. |
