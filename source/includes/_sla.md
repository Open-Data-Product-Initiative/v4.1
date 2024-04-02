# Data SLA

Data Service Level Agreement (SLA) **Object** contains attributes which define the desired and promised quality of the data product. 

No mandatory attributes at the moment. Optional attributes are listed in own table and an example is given in the right column. 

## Optional attributes and elements

> Example of SLA component usage:

```yml

SLA:
- dimension: updateFrequency
  objective: 30
  unit: minutes
  monitoring:
    type: Prometheus 
    spec: | # expressed as string or inline yaml 
      time() - max_over_time(timestamp(changes(table[5m]) > 0)[1d:1m])

- dimension: uptime
  objective: 99.9
  unit: percentage
  monitoring:
    type: Prometheus 
    spec: | # expressed as string or inline yaml
      avg_over_time(
        (
          sum without() (up{job="prometheus"})
            or
          (0 * sum_over_time(up{job="prometheus"}[7d]))
        )[7d:5m]
      )      

- dimension: responseTime
  objective: 300
  unit: milliseconds
    monitoring:
    type: Prometheus 
    spec: | # expressed as string or inline yaml
      sum(rate(http_request_duration_seconds_bucket{le="0.3"}[5m])) by (job)

dashboardURL: https://uptime.opendataproducts.org
support:  
  phoneNumber: ''
  phoneServiceHours: ''
  chatURL: ''
  chatServiceHours: ''
  email: support@opendataproducts.org
  emailServiceHours: ''
  guidesURL: ''



```

| <div style="width:150px">Element name</div>   | Type  | Options  | Description  |
|---|---|---|---|
| SLA | element | - | Binds the SLA related elements and attributes together |
| unit | attribute  | Options for *unit* are: milliseconds, seconds, minutes, days, weeks, months, years, never, null. <br/><br/>  | Name of the quality attribute indicating the timely interval how often data is updated. |
| support | element | - | Support element describes how the customer can reach for help in case of difficulties in usage, billing, or otherwise. |
| phoneNumber | string | - | The support phone number |
| phoneServiceHours | string | - | Describes the service hours company provides. Contains information often in week level eg Mon-Fri at 8am - 4pm. |
| chatURL | URL | Valid URL | The URL of chat service to use. Service hours and response time defined in other attributes. |
| chatServiceHours | string | - | Describes the chat service hours company provides. Contains information often in week level eg Mon-Fri at 8am - 4pm. |
| email | string | - | Email information for support requests. |
| emailServiceHours | string | - | Describes the email service hours company provides. Contains information often in week level eg Mon-Fri at 8am - 4pm. |
| guidesURL | URL | Valid URL | URL to the guides offering more information and examples about how to use the data product. Guides might be platform specific. |
| dashboardURL | URL | Valid URL | URL to dashboard application which visualizes product behaviour. This service should support the given indicators. | 


If you see something missing, described inaccurately or plain wrong, or you want to comment the specification, [raise an issue in Github](https://github.com/Open-Data-Product-Initiative/open-data-product-spec-dev/issues)
