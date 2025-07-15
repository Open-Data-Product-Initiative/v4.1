# Data Contract

The `contract` object defines... 


## Optional attributes and elements

> Example of contract object usage:

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
| **contract**  | element | - | Binds together data contract details. You can use both URL and inline (YAML) for data contract content. | 
| **id**  | string | - | UUID of the data contract | 
| **type**  | string | one of: ODCS, DCS | Defines the standard used in data contract. Currently supported options: [ODCS](https://github.com/bitol-io/open-data-contract-standard) and [DCS](https://datacontract.com/). | 
| **contractVersion**  | string | - | Version of the standard used to define the Data Contract. Type attribute defines the standard/specification. NOTE! This is not the possible iterated version of the data contract itself. | 
| **contractURL**  | URL | Valid URL. See more from [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986). | URL pointing to data contract in data contract management service or alike. Optionally you can use _spec_ to add data contract details as YAML inline element. | 
| **spec**  | string | YAML | Inline YAML element to add data contract details instead of using URL. | 