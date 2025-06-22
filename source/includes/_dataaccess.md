# Data Access

Data Access **OBJECT** describes the authorised ability to retrieve, edit, copy or transfer data from IT systems.

## Optional attributes and elements

> Example of Data Access object usage:

```yml

dataAccess:
  default:
    name:
      - en: Access to zipped package
    description: 
      - en: Latest Dataset and Resources
    outputPorttype: file
    format: zip
    accessURL: url to file as zip
  dataonly:
    name:
      - en: Access to latest dataset
    description: 
      - en: Latest Dataset
    outputPorttype: file
    format: CSV
    accessURL: url to file as CSV
  API:
    outputPorttype: API
    authenticationMethod: OAuth
    specification: OAS
    format: JSON
    accessURL: >-
      https://data.cms.gov/data-api/v1/dataset/2/data
    specsURL: >-
      https://data.cms.gov/provr-enrollment/api-docs
    documentationURL: >- 
      https://data.cms.gov/provr-enrollment/docs
  Agent: 
    outputPorttype: AI
    description: 
    - en: MCP interface for structured data access and agent interaction.
    authenticationMethod: Token
    specification: MCP 2025-03-26
    format: MCP
    specsURL: https://urbanpulse.ai/llms.txt
    documentationURL: https://urbanpulse.ai/llms-full.txt
```
| <div style="width:150px">Element name</div>   | Type  | Options  | Description  |
|---|---|---|---|
| **dataAccess** | object | - | Root-level object containing named access configurations. Each key (e.g., `default`, `API`, `Agent`) defines an access method that can be reused across the ODPS YAML. |
| **default** | object | - | This object defines the default access interface and must always be present if dataAccess object is used. The name `default` is fixed and used as the fallback or primary access method. <br/><br/> In the example above, you will see additional user-defined access methods (`dataonly`, `API`, `Agent`) demonstrating how various access interfaces can be added beyond the required `default`. <br/><br/> **Example reference usage:** <br/> `access: $ref: '#/dataAccess/default'`|

| **name** | object | ISO 639-1 language codes (e.g., `en`) | Multilingual name for the access interface. Can be shown in UIs. |
| **description** | object | ISO 639-1 language codes (e.g., `en`) | Multilingual description for the access interface. Supports user understanding. |
| **outputPorttype** | string | file, API, SQL, AI, gRPC, sFTP, etc. | Describes the technical method for delivering data (e.g., `file` for file downloads, `API` for web services). |
| **format** | string | JSON, XML, CSV, Excel, zip, plain text, GraphQL, MCP | Specifies the data format made available through this access channel. |
| **authenticationMethod** | string | OAuth, Token, API key, HTTP Basic, none | Security model required to access the data. |
| **specification** | string | OAS, RAML, Slate, MCP | Defines the type of API or protocol specification used to describe access (e.g., OpenAPI, RAML, or a custom protocol like MCP). |
| **specsURL** | URL | Valid URL | Points to the machine-readable technical documentation (e.g., OpenAPI YAML). |
| **accessURL** | URL | Valid URL | The direct access point to retrieve the data – can be an API endpoint or a file link. |
| **documentationURL** | URL | Valid URL | A human-readable documentation or guide for access setup, authentication steps, or onboarding. |
| **hashType** | string | SHA-1, SHA-2, SHA-256, MD5, etc. | (Optional) Defines hash algorithm used when providing file integrity verification. |
| **checksum** | string | any string | (Optional) File hash/checksum value, useful for verifying data integrity after download. |