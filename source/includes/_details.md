# Data Product Details

The `details` object defines the business and governance details of the data product. Information added in this object often is the main part of the data product details shown in data product catalogues and market places. 


## Mandatory attributes and elements

> Example of details object usage:

```yml
schema: https://opendataproducts.org/v4.0/schema/odps.yaml
version: 4.0
product:
  details: 
    en:
      name: Pets of the year
      productID: 123456are
      visibility: private
      status: draft
      type: dataset
```


| <div style="width:150px">Element name</div>   | Type  | Options  | Description  |
|---|---|---|---|
| **details** | element | product business details | **REQUIRED** Binds together business details in different languages. |
| **en** | element | [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) defined 2-letter codes | **REQUIRED** - **NOTE! This is a dynamic element!** This element binds together other product attributes and expresses the langugage used. In the example this is "en", which indicates that product details are in English. If you would like to use French details, then name the element "fr". The naming of this element follows options (language codes) listed in [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) standard. <br/><br/> You can have product details in multiple languages simply by adding similar sets like the example - just change the binding element name to matching language code. <br/><br/> The pattern to implement multilanguage support for data products was adopted from de facto UI translation practices. The attributes inside this element are commonly rendered in the UI for the consumer and providing a simple way to implement that was the driving reasoning. See for example  [JSON - Multi Language](https://simplelocalize.io/docs/file-formats/multi-language-json/) |
| **name** | string | max length 256 chars | **REQUIRED** The name of the product. |
| **productID**  | string | max length 256 chars | **REQUIRED** Product identifier. |
| **visibility**  | string | one of: private, invitation, organisation, dataspace, public | **REQUIRED** The publicity level eg who can see this product. Private - just the creator. Invitation - visible only to parties explicitly invited. Organisation - visible to all in your organisation. Dataspace - visible to all existent members of the data space. Public - visible to all publicly. |
| **status**  | string | one of: announcement, draft, development, testing, acceptance, production, sunset, retired | **REQUIRED** The status of the product. Lifecycle model discussed in details in here (link). |
| **type** | string |  one of: raw data, derived data, dataset, reports, analytic view, 3D visualisation, algorithm, decision support, automated decision-making, data-enhanced product, data-driven service, data-enabled performance, bi-directional. | **REQUIRED** The type of the product. Options are derived from examples and lists found from academic literature.  | 

> Example of details object usage:

```yml
schema: https://opendataproducts.org/v4.0/schema/odps.yaml
version: 4.0
product:
  details: 
    en:
      name: Pets of the year
      productID: 123456are
      valueProposition: Design a customised petstore using a data product that describes
        pets with their habits, preferences and characteristics.
      description: This is an example of a Petstore product.
      productSeries: Lovely pets data products
      visibility: private
      status: draft
      productVersion: '0.1.0'
      versionNotes: New version with additional details such more accurate pet details
      issues: The current issues include incorrect information in the dog breeds. The
        resolution for these problems is planned for the next     update, scheduled
        to be released on July 15th, 2023.
      categories:
      - pets
      standards:
      - ISO 24631-6
      tags:
      - pet
      brandSlogan: Passion for the data monetization
      type: dataset
      contentSample: https://download.com/pets.json
      logoURL: https://data-product-business.github.io/open-data-product-spec/images/logo-dps-ebd5a97d.png
      OutputFileFormats:
      - JSON
      - XML
      - CSV
      - ZIP
      - PDF
      useCases:
      - useCase:
          useCaseTitle: Build attractive and lucrative petstore!
          useCaseDescription: Use case description how succesfull petstore chain was established in Abu Dhabi
          useCaseURL: https://marketplace.com/usecase1
      recommendedDataProducts:
      - https://marketplace.com/dataproduct.json
      - https://marketplace.com/dataproduct-another.json
```

## Optional attributes and elements

Additional details of the data product. 

| <div style="width:150px">Element name</div>   | Type  | Options  | Description  |
|---|---|---|---|
| **created**  | date | Use [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) | When product was created. | 
| **updated**  | date | Use [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) | When product was last updated. |
| **valueProposition** | string  | text content, max length 512 chars  | This is the product's value proposition. Often one or two sentences and crystallizes the value for the customer. |
| **description** | string | - | The description of the product. Text only. |
| **productSeries** | string | - | A group of products in the product mix which are associated with each other and they can be obtained for the same type of customers or they are marketable for the same type of market place. |
| **categories** | array | - | Comma separated array of categories. |
| **standards** | array | - | Comma separated array of standards related e.g. to data content or quality, such as ISO 8000 or ISO 19131. |
| **tags** | array | - | Comma separates array of tags. |
| **productVersion** | string | The versioning according to [SemVer](https://semver.org/) | The version of the data product. Applies for ODPS metadata as well. |
| **versionNotes** | string | - | Additional information about the version. |
| **issues** | string | - |  There may be errors in the data product that require corrections. These issues will be briefly described to users, along with information about when the fixes will be implemented.|
| **contentSample** | URL | Valid URL. See more from [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986). | Sample content of the data product, for example JSON/XML output. This sample should match the actual data product output and give the data consumer an idea what to expect. Obviously if the data product is pure service for example dashboard or algorithm, then consider providing preview version or alike |
| **logoURL** | URL | Valid URL | Valid URL of the logo. See more from [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986). |
| **outputFileFormats** | string | - | Output file formats for data product |
| **brandSlogan** | string | - | Brand related slogan like Nike has *just do it*. |
| **useCases** | element | array | Contains list of related use cases with description information and link to details. **NOTE!** These examples are expected to use same language as defined previously in the data product details content binding element. |
| **useCaseTitle**| string | string | Title of the usecase. |
| **useCaseDescription** | string | - | Brief description of the usecase. |
| **useCaseURL**| URL | Valid URL, [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986) | Valid URL of the more detailed usecase description. |
| **recommendedDataProducts** | array | Array of valid URLs ([RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986)) | Data products to recommend use next to this data product or even as replacement (for comparison). The URL provided MUST reference a description of a data product following this same standard |

If you see something missing, described inaccurately or plain wrong, or you want to comment the specification, [raise an issue in Github](https://github.com/Open-Data-Product-Initiative/dev/issues)