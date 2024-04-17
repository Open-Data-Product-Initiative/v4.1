# Data SLA

Data Service Level Agreement (SLA) **Object** contains attributes which define the desired and promised quality of the data product. SLA can be defined with 11 dimentions: 

1. latency, 
1. uptime, 
1. responseTime, 
1. errorRate, 
1. endOfSupport, 
1. endOfLife, 
1. updateFrequency, 
1. timeToDetect, 
1. timeToNotify, 
1. timeToRepair, 
1. emailResponseTime. 

Each dimension has objective value, a unit and then monitoring "as code" to verify objective. In some cases monitoring is 
not feasable or possible to arrange for various reasons. Type attribute indicates which monitoring system is used. Reference attribute contains url for reference documentation regarding the monitoring spec. Spec contains the actucal "as code" part which can be executed in selected monitoring system as is. 

No mandatory attributes at the moment. Optional attributes are listed in own table and an example is given in the right column. 

## Optional attributes and elements

> Example of SLA component usage:

```yml

SLA:
  - dimension: latency
    objective: 100
    unit: milliseconds
    monitoring:
      type: prometheus
      reference: https://prometheus.io/docs/prometheus/latest/querying/basics/ 
      spec:  
        myTimer.observeDuration();

  - dimension: uptime
    objective: 99
    unit: percent
    
  - dimension: responseTime
    objective: 200
    unit: milliseconds
    monitoring:
      type: prometheus
      reference: https://prometheus.io/docs/prometheus/latest/querying/basics/ 
      spec:  
       rate(http_server_requests_seconds_sum[$__rate_interval]) / rate(http_server_requests_seconds_count[$__rate_interval])

  - dimension: errorRate
    objective: 0.1
    unit: percent
  
  - dimension: endOfSupport
    objective: 01/01/2025 # dd/mm/yyyy
    unit: date

  - dimension: endOfLife
    objective: 01/03/2025 # dd/mm/yyyy
    unit: date

  - dimension: updateFrequency
    objective: 7
    unit: days

  - dimension: timeToDetect
    objective: 60
    unit: minutes

  - dimension: timeToNotify
    objective: 120
    unit: minutes

  - dimension: timeToRepair
    objective: 24
    unit: hours

  - dimension: emailResponseTime
    objective: 12
    unit: hours

  support:
      phoneNumber: '+971508976456'
      phoneServiceHours: 'Mon-Fri 8am-4pm (GMT)'
      email: support@opendataproducts.org
      emailServiceHours: 'Mon-Fri 8am-4pm (GMT)'
      documentationURL: ''
```



| <div style="width:150px">Element name</div>   | Type  | Options  | Description  |
|---|---|---|---|
| SLA | element | - | Binds the SLA related elements and attributes together |
| dimension | attribute | string, one of | Defines the SLA dimension. Can be one of: latency, uptime, responseTime, errorRate, endOfSupport, endOfLife, updateFrequency, timeToDetect, timeToNotify, timeToRepair, emailResponseTime  |
| unit | attribute  | Options for *unit* are: milliseconds, seconds, minutes, days, weeks, months, years, never, date, null. <br/><br/>  | Name of the quality attribute indicating the timely interval. If date is given, format is dd/mm/yyyy |
| support | element | - | Support element describes how the customer can reach for help in case of difficulties in usage, billing, or otherwise. |
| phoneNumber | string | - | The support phone number |
| phoneServiceHours | string | - | Describes the service hours company provides. Contains information often in week level eg Mon-Fri at 8am - 4pm. |
| email | string | - | Email information for support requests. |
| emailServiceHours | string | - | Describes the email service hours company provides. Contains information often in week level eg Mon-Fri at 8am - 4pm. |
| documentationURL | URL | Valid URL | URL to documentation | 


If you see something missing, described inaccurately or plain wrong, or you want to comment the specification, [raise an issue in Github](https://github.com/Open-Data-Product-Initiative/open-data-product-spec-dev/issues)
