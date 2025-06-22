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
    accessURL: >-
      https://data.cms.gov/data-api/v1/dataset/2/data
    specsURL: >-
      https://data.cms.gov/provr-enrollment/api-docs
    documentationURL: >- 
      https://data.cms.gov/provr-enrollment/docs
```

| <div style="width:150px">Element name</div>   | Type  | Options  | Description  |
|---|---|---|---|
| **dataAccess** | element | - |  Binds the data access related elements and attributes together. |
| **interface** | element | - | Reference to the ability to use data. |
| **outputPorttype** | string | any  | 	Type of data access, such as API, SQL, sFTP, gRPC. |
| **hashType** | string | any | Type of secure hash algorithm, such as SHA-1, SHA-2, for checksum, when output is file(s).  |
| **checksum** | string | any | File checksum. |
| **authenticationMethod** | string | any  | Data access authentication method type, such as API key, HTTP Basic, OAuth, No authentication. |
| **specification** | string | any  | Type of the data access specification, such as OAS, RAML, Slate. |
| **format** | string | any | 	Data access file format type, such as JSON, XML, GraphQL, plain text. |
| **specsURL** | URL | Valid URL | 	The URL of the data access documentation, preferably in a machine-readable format, such as OpenAPI specs. |
| **acccessURL** | URL | Valid URL | 	The URL of direct data access. Can be API endpoint or file  |
| **documentationURL** | URL | Valid URL  | The URL of the separated data access documentation or guide. For example, it may contain instructions on how to create and manage api keys.|
