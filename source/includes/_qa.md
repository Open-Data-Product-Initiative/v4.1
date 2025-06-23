# Data Quality

> Template structure of Data Quality array component:

```yml
dataQuality:
  declarative:
    default:
      dimensions:
        - dimension: accuracy
          displaytitle:
            en: Data Accuracy (percent)
          objective: 90
          unit: percentage
        - dimension: completeness
          displaytitle:
            - en: Data Completeness (percent)
          objective: 90
          unit: percentage
  executable:
    - dimension: selected dimension
      type:  
      version: 
      reference: 
      spec:
```

> In case standardized options are not enough:

```yml
The QA object is general in nature and should 
be enough for common (80%) use cases. 

You can make extensions to the standard 
with "x-" mechanism in order to fulfill 
any industry specific needs. 

A suggestive example below 

dataQuality:
  declarative:
    default:
      dimensions:
        - dimension: accuracy
          displaytitle:
            en: Data Accuracy (percent)
          objective: 90
          unit: percentage
        - x-dimension: extended-dq
          displaytitle:
            en: Extended Data Quality dimension
          
```

Data quality is essential for one main reason: You give customers the best experience when you make decisions using accurate data. A great customer experience leads to happy customers, brand loyalty, and higher revenue for your business. Information is only valuable if it is of high quality.  

By adhering to defined quality characteristics, organizations can maximize the value of their data assets, improve decision-making, enhance operational efficiency, and maintain trust and confidence in their data-driven processes and systems. ODPS is compatible with EDM Council data quality model.

How can you assess your data quality? The ODPS support "as code" approach to monitor data quality. Supported DQ tools for Everything as Code to define monitoring are: 

* SodaCL
* MonteCarlo
* DQOps
* Custom (in-house solutions)

**Structure notes:** The Data Quality object is divided into 2 parts: declarative and executable. 

* Declarative part defines the dimensions and aimed/intended data quality levels in defined unit. 
* Executable part contains the machine-readable "as code" rules to validate data quality dimensions. The code inside _spec_ element is intended to be injected as in supporting data quality platforms in their defined format and structure.  

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

## Referencing Examples

To reference a defined quality profile from another part of your YAML (e.g., pricing plan): _$ref: '#/dataQuality/default'_. Or reference a named premium quality package: _$ref: '#/dataQuality/premium'_ Use this component to clearly communicate both intentions and verifiable guarantees about data quality—whether you're reporting to stakeholders, building trust with customers, or enabling automated validation through modern DQ tools. 


## Optional attributes and elements

> Example of Data Quality component with some of the data quality dimensions:

```yml
dataQuality:
  declarative:
    default:
      displaytitle: 
        en: The Basic Data Quality
      description: 
        en: The basic quality package
      dimensions:
        - dimension: accuracy
          displaytitle:
            en: Data Accuracy (percent)
          description:
            en: >
              Data Accuracy ensures the data product reflects the real-world
              entities or events it represents, minimizing errors and providing
              reliable insights.
          objective: 90
          unit: percentage
        - dimension: completeness
          displaytitle:
            - en: Data Completeness (percent)
          objective: 90
          unit: percentage


    premium:
      displaytitle: 
        en: The Premium Data Quality
      description: 
        en: The Preimum quality package
      dimensions:
        - dimension: accuracy
          displaytitle:
            en: Data Accuracy (percent)
          description:
            en: >
              Data Accuracy ensures the data product reflects the real-world
              entities or events it represents, minimizing errors and providing
              reliable insights.
          objective: 98
          unit: percentage
        - dimension: completeness
          displaytitle:
            en: Data Completeness (percent)
          objective: 99
          unit: percentage

  executable:
    - dimension: accuracy
      type: SodaCL
      reference: https://docs.soda.io/soda-cl/soda-cl-overview.html
      spec:
        - require_unique(member_id) 
        - require_range(age_band, 18, 100)
    - dimension: completeness
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
```


| <div style="width:150px">Element name</div>   | Type  | Options  | Description  |
|---|---|---|---|
| **dataQuality** | element | - | Contains array of data quality dimensions with optional computational monitoring object. Under this element Data Quality is divided into declarative and executable parts. |
| **default** | object | - | This object must always be present and named exactly `default` if dataQuality object is used. It acts as the fallback or primary data quality profile. <br/><br/>Users are free to define additional named profiles such as `premium`, `gold`, etc., in parallel to the default. <br/><br/>In the example, `default` and `premium` are both included. These variants can be referred to from other components like pricing plans. <br/><br/>**Example reference usage:** <br/> `dataQuality: $ref: '#/dataQuality/default'` |
| **dimension** | attribute | string, one of: *accuracy, completeness, conformity, consistency, coverage, timeliness, validity, or uniqueness.* | Defines the data quality dimension. |
| **objective** | attribute | integer | Defines the target value for the data quality dimension |
| **unit** | attribute | string. One of: *percentage, number* | Defines the unit used in stating the target quality level. |
| **executable** | element | - | Grouping element that collects together data quality monitoring rules. You can define monitoring patterns as code under this element for each dimension. The actual as-code part is defined in the `spec` element. |
| **displaytitle** | array | - | Dimension title to be shown in various UIs. Array contains title(s) in desired language(s). |
| **en** | attribute | [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) defined 2-letter codes | Binds the text elements together in a given language. Multilanguage support is implemented by duplicating content under other ISO language codes. |
| **description** | array | - | Describe the dimension so that it can be used for example in info boxes in UI. Array contains descriptions in desired language(s). |
| **type** | attribute | string, one of: [SodaCL](https://docs.soda.io/soda-cl/soda-cl-overview.html), [Montecarlo](https://docs.getmontecarlo.com/docs/monitors-as-code), [DQOps](https://dqops.com/docs/categories-of-data-quality-checks/), Custom | Data Quality Monitoring as code system name. Use one of the predefined options only. With _Custom_ type you can use your in-house solution. |
| **version** | attribute | string | The version of DQ monitoring tool used. |
| **reference** | URL | Valid URL | Provide URL pointing to the reference documentation. |
| **spec** | element | YAML/URL/string | The content for Data Quality monitoring expressed as code. Accepted as inline YAML, a valid URL pointing to YAML, or a plain string if `type` is `Custom`. |




If you see something missing, described inaccurately or plain wrong, or you want to comment the specification, [raise an issue in Github](https://github.com/Open-Data-Product-Initiative/dev/issues)
