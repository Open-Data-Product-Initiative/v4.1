# Data Quality

Data quality is essential for one main reason: You give customers the best experience when you make decisions using accurate data. A great customer experience leads to happy customers, brand loyalty, and higher revenue for your business. Information is only valuable if it is of high quality.  How can you assess your data quality? Data quality meets six dimensions: accuracy, completeness, consistency, timeliness, validity, and uniqueness. 

The values of the QA attributes are given by the vendor. Should you trust in the values, is the choice made by the data consumer. If possbile utilize automatic checking of data quality against the source and update the values accordingly. 

The QA object is general in nature and should be enough for common (80%) of the use cases. Note that you can make extensions to the standard with "x-" mechanism in order to fulfill any industry specific needs. The "Specification extensions" section provides details on how to use this feature. 

Data integrity is the maintenance of, and the assurance of, data accuracy and consistency over its entire life-cycle. That is why *integrity* is not in the attributes, but accuracy and consistency as well as completeness are. 

## Optional attributes and elements

> Example of Data Quality component with some of the voluntary attributes:

```javascript
   "dataQuality":{
      "accuracy":100,
      "completeness":100,
      "consistency":100,
      "timeliness":"high",
      "validity":100,
      "uniqueness":100,
      "dataQualityAssuranceMethods":"Data quality assurance suite of tools and methods include both data quality auditing (DQA) tools designed for use by external audit teams and routine data quality assessment (RDQA) tools designed for capacity building and self-assessment.",
      "dataQualityMonitoring":"SodaCL",
      "monitoringScriptURL":"http://192.168.10.1/soda-petshop.py"
      }
      
```

| <div style="width:150px">Element name</div>   | Type  | Options  | Description  |
|---|---|---|---|
| dataQuality | element | - | Binds the data quality related elements and attributes together |
| accuracy | integer  | percentage | The term “accuracy” refers to the degree to which information accurately reflects an event or object described. For example, if a customer’s age is 32, but the system says she’s 34, that information is inaccurate. |
| completeness | integer | percentage | Data is considered “complete” when it fulfills expectations of comprehensiveness. Let’s say that you ask the customer to supply his or her name. You might make a customer’s middle name optional, but as long as you have the first and last name, the data is complete. |
| consistency | integer | percentage | At many companies, the same information may be stored in more than one place. If that information matches, it’s considered “consistent.” For example, if your human resources information systems say an employee doesn’t work there anymore, yet your payroll says he’s still receiving a check, that’s inconsistent. |
| timeliness | string | one of: low, medium, high | Is your information available right when it’s needed? That data quality dimension is called “timeliness.” Let’s say that you need financial information every quarter; if the data is ready when it’s supposed to be, it’s timely. The data quality dimension of timeliness is a user expectation.  |
| validity | integer | percentage | Validity is a data quality dimension that refers to information that doesn’t conform to a specific format or doesn’t follow business rules. A popular example is birthdays – many systems ask you to enter your birthday in a specific format, and if you don’t, it’s invalid. To meet this data quality dimension, you must check if all of your information follows a specific format or business rules. |
| uniqueness | integer | percentage | “Unique” information means that there’s only one instance of it appearing in a database. As we know, data duplication is a frequent occurrence. “Daniel A. Robertson” and “Dan A. Robertson” may well be the same person. Meeting this data quality dimension involves reviewing your information to ensure that none of it is duplicated. |
| dataQualityAssuranceMethods | string | text content, max length 512 chars | Description of the data product quality assurance methods and tools used. Promotes data reliability engineering as-code approach. |
| dataQualityMonitoring | string | text content, max length 512 chars |  The tool used for assessing data quality, like [Soda tools: SodaCL](https://docs.soda.io/soda-cl/soda-cl-overview.html) or SQL queries. |
| monitoringScriptURL | URL | valid URL | The URL of the data quality assessment and monitoring script.  |



<button data-tf-popup="Q1Zo6wE5" data-tf-iframe-props="title=Customer Feedback Survey" style="all:unset;font-family:Helvetica,Arial,sans-serif;display:inline-block;max-width:100%;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;background-color:#FA6B05;color:#000000;font-size:17px;border-radius:3px;padding:0 28px;font-weight:bold;height:42.5px;cursor:pointer;line-height:42.5px;text-align:center;margin:0;text-decoration:none;">Raise an issue</button><script src="//embed.typeform.com/next/embed.js"></script>
