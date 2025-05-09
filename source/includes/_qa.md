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


## Optional attributes and elements

> Example of Data Quality:

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
