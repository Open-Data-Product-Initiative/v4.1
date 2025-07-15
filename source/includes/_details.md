# Data product details

The `details` object defines... 


## Optional attributes and elements

> Example of details object usage:

```yml
schema: https://opendataproducts.org/v4.0/schema/odps.yaml
version: 4.0
product:
  contract:
    id: 02323M123  
    type:  ODCS 
    contractVersion:  2.2.2
    contractURL: https://demo.datamesh-manager.com/demo834016807886/dataproducts/9bd53b1b-b51e-41a8-a757-4d33b4cde460


```

> Example of contract ref usage:

```yml

contract: # the below file contains the same content as above contract element
  $ref: 'https://example.org/contracts/default.yaml'

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