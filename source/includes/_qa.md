# Data Quality

Data quality is essential for one main reason: You give customers the best experience when you make decisions using accurate data. A great customer experience leads to happy customers, brand loyalty, and higher revenue for your business. Information is only valuable if it is of high quality.  How can you assess your data quality? Data quality meets six dimensions: accuracy, completeness, consistency, timeliness, validity, and uniqueness. 

The values of the QA attributes are given by the vendor. Should you trust in the values, is the choice made by the data consumer. If possbile utilize automatic checking of data quality against the source and update the values accordingly. 

The QA object is general in nature and should be enough for common (80%) of the use cases. Note that you can make extensions to the standard with "x-" mechanism in order to fulfill any industry specific needs. The "Specification extensions" section provides details on how to use this feature. 

Data integrity is the maintenance of, and the assurance of, data accuracy and consistency over its entire life-cycle. That is why *integrity* is not in the attributes, but accuracy and consistency as well as completeness are. 

## Optional attributes and elements

> Example of Data Quality component with some of the voluntary attributes:

```yml

dataQuality:
  - dimension: accuracy
    objective: 98
    unit: percentage
    monitoring:
      type: SodaCL 
      spec:
        - require_unique(member_id) 
        - require_range(age_band, 18, 100)
  - dimension: completeness
    objective: 98
    unit: percentage
    monitoring:
      type: SodaCL 
      spec:
        - for each column:
            name: [member_id, gender, age_band]
            checks:
              - not null:
                  fail: when > 2% # Fail if more than 2% of records are null
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
| dataQuality | element | - | Contains array of data quality dimensions with optional computational monotoring object. Binds the data quality related elements and attributes together |
| dimension | attribute | string, one of | Defines the data quality dimension. Can be one of: accuracy, completeness, consistency, timeliness, validity, or uniqueness  |
| objective | attribute | integer | Defines the target value for the data quality dimension |
| unit | attribute | string | Defines the unit used in stating the target quality level. One of: percentage, number |
| monitoring | element | - | Contains the monitoring (computational "as code") structure to validate target state for the selected data quality dimension. |
| type | attribute | string | monitoring system name name such as SodaCL and Montecarlo. The systems enable as code approach to monitor data quality. |
| spec | element | - | contains the as code part for monitoring. Content is intended to be in a form that can be injected as is to defined monitoring system. |



If you see something missing, described inaccurately or plain wrong, or you want to comment the specification, [raise an issue in Github](https://github.com/Open-Data-Product-Initiative/open-data-product-spec-dev/issues)
