# Data Access

Data Access **OBJECT** describes the authorised ability to retrieve, edit, copy or transfer data from IT systems.

## Optional attributes and elements

> Example of Data Access object usage:

```yml

dataAccess:
  - interface: filecollection
    description: 
      en: Latest Dataset and Resources
    outputPorttype: file
    format: zip
    accessURL: url to file as zip
  - interface: dataonly
    description: 
      en: Latest Dataset and Resources
    outputPorttype: file
    format: CSV
    accessURL: url to file as CSV
  - interface: API
    authenticationMethod: OAuth
    specification: OAS
    format: JSON
    accessURL: >-
      https://data.cms.gov/data-api/v1/dataset/2/data
    specsURL: >-
      https://data.cms.gov/provr-enrollment/api-docs
    documentationURL: >- 
      https://data.cms.gov/provr-enrollment/docs
  - name: Agent 
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
| **dataAccess** | element | - |  Binds the data access related elements and attributes together. |
| **interface** | element | - | Reference to the ability to use data. Use simple name, it will be references from other objects like Pricing |
| **outputPorttype** | string | any  | 	Type of data access, such as API, SQL, sFTP, gRPC. |
| **hashType** | string | any | Type of secure hash algorithm, such as SHA-1, SHA-2, for checksum, when output is file(s).  |
| **checksum** | string | any | File checksum. |
| **authenticationMethod** | string | any  | Data access authentication method type: API key, HTTP Basic, OAuth, No authentication. |
| **specification** | string | any  | Type of the data access specification, such as OAS, RAML, Slate. |
| **format** | string | any | 	Data access file format type: JSON, XML, GraphQL, plain text, zip, CSV, Excel. |
| **specsURL** | URL | Valid URL | 	The URL of the data access documentation, preferably in a machine-readable format, such as OpenAPI specs. |
| **acccessURL** | URL | Valid URL | 	The URL of direct data access. Can be API endpoint or file  |
| **documentationURL** | URL | Valid URL  | The URL of the separated data access documentation or guide. For example, it may contain instructions on how to create and manage api keys.|
