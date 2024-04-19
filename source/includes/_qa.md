# Data Quality

Data quality is essential for one main reason: You give customers the best experience when you make decisions using accurate data. A great customer experience leads to happy customers, brand loyalty, and higher revenue for your business. Information is only valuable if it is of high quality.  How can you assess your data quality? ODPS is compatible with EDM Council data quality model. 

**ODPS offers 8 options to define and measure data quality:** 

| <div style="width:150px">Data Quality Dimension</div>   | Description | 
|---|---|
| **accuracy** | Desc |
| **completeness** | Desc |
| **conformity** | Desc |
| **consistency** | Desc |
| **coverage** | Desc |
| **timeliness** | Desc |
| **validity** | Desc |
| **uniqueness** | Desc |


The above list most likely covers majority of the cases and needs of organizations. In case additional indicators are needed, then use specification extensions (x-) described in the specification separately. 

The values of the QA attributes are given by the vendor. Should you trust in the values, is the choice made by the data consumer. If possible utilize automatic checking of data quality against the source and update the values accordingly. 

The QA object is general in nature and should be enough for common (80%) of the use cases. Note that you can make extensions to the standard with "x-" mechanism in order to fulfill any industry specific needs. The "Specification extensions" section provides details on how to use this feature. 

Data integrity is the maintenance of, and the assurance of, data accuracy and consistency over its entire life-cycle. That is why *integrity* is not in the attributes, but accuracy and consistency as well as completeness are. 

**Note!** The "as code" *spec* part of the component is the initial step towards embracing Everything as Code paradigm, but is still experimental. We need more vendors supporting the approach. In the mean while you can use custom solutions. 

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
    - en: Data Completeness
    objective: 99.9
    unit: percentage
    monitoring:
      type: SodaCL 
      reference: https://docs.soda.io/soda-cl/soda-cl-overview.html
      spec:
        - for each column:
            name: [member_id, gender, age_band]
            checks:
              - not null:
                  fail: when > 0.1% # Fail if more than 0.1% of records are null

  - dimension: consistency
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
| **type** | attribute | string | monitoring system name name such as SodaCL and Montecarlo. The systems enable as code approach to monitor data quality. |
| **reference** | URL | Valid URL | Provide URL for the reference documentation |
| **spec** | element | - | contains the as code part for monitoring. Content is intended to be in a form that can be injected as is to defined monitoring system. Content depends of the system used and reference attribute is expected to provide more information. |



If you see something missing, described inaccurately or plain wrong, or you want to comment the specification, [raise an issue in Github](https://github.com/Open-Data-Product-Initiative/open-data-product-spec-dev/issues)
