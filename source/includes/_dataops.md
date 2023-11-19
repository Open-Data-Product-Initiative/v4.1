# DataOps

DataOps is a process whereby a data product pipeline deployment method is defined. Usually the deployment script contains the logic of the individual steps as well as the code chaining the steps together.

DataOps **OBJECT** describes building, deploying, and running data product's code, and storing and giving access to data and metadata. This principle has been adopted from the [Data Mesh](https://towardsdatascience.com/what-is-a-data-mesh-and-how-not-to-mesh-it-up-210710bb41e0).

> Example of DataOps component usage:

```javascript
  
"dataOps":{
  "infrastructure":{
    "platform":"Azure",
    "region": "West US 2 (Washington)";
    "storageTechnology":"Azure SQL",
    "storageType":"sql",
    "containerTool":"helm",
    "format":"yaml",
    "schemaLocationURL":"http://http://192.168.10.1/schemas/2016/petshopML-2.3/schema/petstore.xsd",
    "scriptURL":"http://192.168.10.1/rundatapipeline.yml",
    "deploymentDocumentationURL":"http://192.168.10.1/datapipeline",
    "dataLineageTool":"Collibra",
    "dataLineageOutput":"http://192.168.10.1/lineage.json",
    "hashType":"SHA-2",
    "checksum":"7b7444ab8f5832e9ae8f54834782af995d0a83b4a1d77a75833eda7e19b4c921",
    "signatureType": "JWK"
  }
}
  
```
| <div style="width:150px">Element name</div>   | Type  | Options  | Description  |
|---|---|---|---|
| dataOps | element | - |  Binds the dataOps related elements and attributes together. |
| infrastructure | element | - | Infrastructure is a process whereby a data product pipeline deployment method is defined. |
| platform | string | any | Platform infrastructure, such as AWS, GCP, Azure. |
| region | string | any | Provide details of cloud region of AWS, Azure or alike. Examples for AWS: US West (Oregon), Canada (Central), US East (N. Virginia), US East (Ohio). Examples for Azure: Canada Central (Toronto), East US 2 (Virginia), West US 2 (Washington) |
| storageTechnology | string | any | Describes the internal storage area technology, such as Amazon S3, Google Cloud Storage, Azure Blob Storage, Azure SQL. |
| storageType | string | any | Describes the internal storage type, such as files, sql, events, MQTT. |
| containerTool | string | any | A name of the package manager, container or infrastructure as code tool. |
| format | string  | any |  Type of script language.|
| schemaLocationURL | URL  | Valid URL |  The URL of the data product schema, such as XSD, XML or JSON Schema. |
| scriptURL | URL | Valid URL  | 	The URL of the deployment script. Script can be used for implementing the data product. In a Data Mesh -model it can be used to define, for example, one or more outputs which take the data from source systems or other data products.|
| deploymentDocumentationURL | URL | Valid URL  | 	The URL of the deployment documentation. |
| datalineageTool | URL | Valid URL  | 	A tool to view the data lineage. |
| datalineageOutput | URL | Valid URL  | 	The URL of the data lineage output. Data lineage output shows the mapping of source data to target output on a metadata level |
| hashType| string | One of: SHA-1, SHA-2, SHA-3 | Type of secure hash algorithm for checksum. |
| checksum| string | any  | 	Script checksum. |
| signatureType| string | any  | A public-key cryptosystem,such as JWK, PKCS#12, or PEM. |
