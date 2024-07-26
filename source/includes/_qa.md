# Data Quality

Data quality is essential for one main reason: You give customers the best experience when you make decisions using accurate data. A great customer experience leads to happy customers, brand loyalty, and higher revenue for your business. Information is only valuable if it is of high quality.  

By adhering to defined quality characteristics, organizations can maximize the value of their data assets, improve decision-making, enhance operational efficiency, and maintain trust and confidence in their data-driven processes and systems. ODPS is compatible with EDM Council data quality model.

How can you assess your data quality? The ODPS support "as code" approach to monitor data quality. Supported DQ tools for Everything as Code to define monitoring are: 

* SodaCL
* MonteCarlo
* DQOps
* Custom (in-house solutions)



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


> Template structure of Data Quality array component:

```yml
 - dimension: selected dimension
    objective: 
    unit: 
    monitoring:
      type:  
      version: 
      reference: 
      spec:
      
```

Each dimension has objective value, a unit and then *monitoring* "as code" to verify objective. In some cases monitoring is 
not feasable or possible to arrange for various reasons. *Type* attribute indicates which monitoring system is used. *Reference* attribute contains url for reference documentation regarding the monitoring spec. *Spec* contains the monitoring rules "as code" to be executed in selected monitoring system as is.  

**Note!** The "as code" part of the component is the initial step towards embracing Everything as Code paradigm, but is still experimental. We need more vendors supporting the approach. You can use predefined vendor options (as type) and custom for in-house solutions.

The QA object is general in nature and should be enough for common (80%) use cases. Note that you can make extensions to the standard with "x-" mechanism in order to fulfill any industry specific needs. The ["Specification extensions"](#specification-extensions) section provides details on how to use this feature. 

Data integrity is the maintenance of, and the assurance of, data accuracy and consistency over its entire life-cycle. That is why *integrity* is not in the attributes, but accuracy and consistency as well as completeness are. 
  

## Optional attributes and elements

> Example of Data Quality component with some of the data quality dimensions:

```yml

dataQuality:
  - dimension: accuracy
    displaytitle:
    - en: Data Accuracy (percent)
    - fi: Datan virheettömyys (prosenttia)
    objective: 98
    unit: percentage
    monitoring:
      type: SodaCL
      reference: https://docs.soda.io/soda-cl/soda-cl-overview.html
      spec:
        - require_unique(member_id) 
        - require_range(age_band, 18, 100)

  - dimension: completeness
    displaytitle:
    - en: Data Completeness (percent)
    objective: 90
    unit: percentage
    monitoring:
      type: DQOps
      version: 1.6.0 
      reference: https://dqops.com/docs/dqo-concepts/running-data-quality-checks/
      spec:
        columns:
          target_column:
            profiling_checks: 
              nulls: 
                profile_nulls_percent: 
                  warning: 
                    max_percent: 8.0
                  error: 
                    max_percent: 10.0
                  fatal: 
                    max_percent: 11.0


  - dimension: consistency
    displaytitle:
    - en: Data Consistency (percent)
    - fi: Datan johdonmukaisuus (prosenttia)
    objective: 98
    unit: percentage
      
  - dimension: timeliness
    objective: 100
    unit: percentage

  - dimension: validity
    objective: 98
    unit: percentage

  - dimension: uniqueness
    objective: 100
    unit: percentage
      
```

| <div style="width:150px">Element name</div>   | Type  | Options  | Description  |
|---|---|---|---|
| **dataQuality** | element | - | Contains array of data quality dimensions with optional computational monotoring object. Binds the data quality related elements and attributes together |
| **dimension** | attribute | string, one of: *accuracy, completeness, conformity, consistency, coverage, timeliness, validity, or uniqueness.* | Defines the data quality dimension.  |
| **objective** | attribute | integer | Defines the target value for the data quality dimension |
| **unit** | attribute | string. One of: *percentage, number* | Defines the unit used in stating the target quality level. |
| **monitoring** | element | - | Contains the monitoring (computational "as code") structure to validate target state for the selected data quality dimension. |
| **displayTitle** | array| - | Dimension title to be shown is various UIs. Array contains array list of titles in desired amount of languages. |
| **en** | attribute | [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) defined 2-letter codes | This element binds together other product attributes and expresses the langugage used. In the example this is "en", which indicates that product details are in English. If you would like to use French details, then name the element "fr". The naming of this element follows options (language codes) listed in [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) standard. <br/><br/> You can have product details in multiple languages simply by adding similar sets like the example - just change the binding element name to matching language code. <br/><br/> The pattern to implement multilanguage support for data products was adopted from de facto UI translation practices. The attributes inside this element are commonly rendered in the UI for the consumer and providing a simple way to implement that was the driving reasoning. See for example  [JSON - Multi Language](https://simplelocalize.io/docs/file-formats/multi-language-json/) |
| **type** | attribute | string, one of: [SodaCL](https://docs.soda.io/soda-cl/soda-cl-overview.html), [Montecarlo](https://docs.getmontecarlo.com/docs/monitors-as-code), [DQOps](https://dqops.com/docs/categories-of-data-quality-checks/), Custom | DAta Quality Monitoring as code system name. Use one of the predefined options only. With _Custom_ type you can use your in-house solution. |
| **version** | attribute | string | The version of DQ monitoring tool used. |
| **reference** | URL | Valid URL | Provide URL pointing to the reference documentation |
| **spec** | element | YAML/URL/string | The content the as code part for Data Quality monitoring. Content is intended to be in a form that can be injected as is to _type_ defined monitoring system. Content depends of the system used and reference attribute is expected to provide more information. <br/><br/> **Note!** By default the rules must be provide as valid YAML, either as inline element (YAML) or as valid URL (filesystem or online) pointing to valid YAML content file. String content is allowed and used only if _type_ attribute value is _Custom_. In the custom case your string of course can be YAML too. |


If you see something missing, described inaccurately or plain wrong, or you want to comment the specification, [raise an issue in Github](https://github.com/Open-Data-Product-Initiative/dev/issues)
