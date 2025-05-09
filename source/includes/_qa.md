# Data Quality

> Template structure of Data Quality array component:

```yml
dataQuality:
  promise:
    $ref: "#/Components/DataQualities/Basic"
  monitoring:
    $ref: "#/Components/DataQualities/Basic/Monitoring"
```



Data quality is essential for one main reason: You give customers the best experience when you make decisions using accurate data. A great customer experience leads to happy customers, brand loyalty, and higher revenue for your business. Information is only valuable if it is of high quality.  

By adhering to defined quality characteristics, organizations can maximize the value of their data assets, improve decision-making, enhance operational efficiency, and maintain trust and confidence in their data-driven processes and systems. ODPS is compatible with EDM Council data quality model.

How can you assess your data quality? The ODPS support "as code" approach to monitor data quality. Supported DQ tools for Everything as Code to define monitoring are: 

**Structure notes:** The Data Quality object is divided into 2 parts: promise and monitoring. 

* Promise part defines the dimensions and aimed/intended data quality levels in defined unit. 
* Monistoring part contains the machine-readable "as code" rules to validate data quality dimensions. The code inside _spec_ element is intended to be injected as in supporting data quality platforms in their defined format and structure.  

The QA object is general in nature and should be enough for common (80%) use cases. Note that you can make extensions to the standard with "x-" mechanism in order to fulfill any industry specific needs. The ["Specification extensions"](#specification-extensions) section provides details on how to use this feature. 

## ODPS offers 8 standardized options to define and measure data quality with Everything as Code monitoring 



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


Data integrity is the maintenance of, and the assurance of, data accuracy and consistency over its entire life-cycle. That is why *integrity* is not in the attributes, but accuracy and consistency as well as completeness are. 
  

## Optional attributes and elements

> Example of Data Quality component with some of the data quality dimensions:

```yml
dataQuality:
  promise:
    $ref: "#/Components/DataQualities/Basic"
  monitoring:
    $ref: "#/Components/DataQualities/Basic/Monitoring"    
```

| <div style="width:150px">Element name</div>   | Type  | Options  | Description  |
|---|---|---|---|
| **dataQuality** | element | - | - |
| **promise** | element | - | Contains reference to data quality component to use  |
| **monitoring** | element | - | Contains reference to data quality monitoring component to use |


If you see something missing, described inaccurately or plain wrong, or you want to comment the specification, [raise an issue in Github](https://github.com/Open-Data-Product-Initiative/dev/issues)
