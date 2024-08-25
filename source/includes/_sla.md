# Data SLA

> Template structure of SLA array component:

```yml
declarative:
  - dimension: selected dimension
    displaytitle:
    description:
    objective: 
    unit:
executable:
  - dimension: selected dimension
    type:  
    version: 
    reference: 
    spec:
```

Data Service Level Agreement (SLA) **Object** contains attributes which define the desired and promised quality of the data product. 

A Data Service Level Agreement (SLA) is a contractual agreement between a data service provider and its customers that defines the expected level of service quality, performance, and availability for the data services provided. SLAs outline specific metrics, targets, and responsibilities that both parties agree to adhere to, ensuring accountability and transparency in the delivery of data services.

Defining Data SLAs in a machine-readable format enhances automation, facilitates monitoring, enables real-time compliance tracking, and supports seamless integration with monitoring and alerting systems.

**Structure notes:** The SLA object is divided into 2 parts: declarative and executable. Declarative part defines the dimensions and aimed/intended SLA levels in defined unit. Executable part contains the machine-readable "as code" rules to validate SLA dimensions. The code inside _spec_ element is intended to be injected as in supporting SLA monitoring platforms in their defined format and structure.  

> In case standardized options are not enough:

```yml
The SLA object is general in nature and should 
be enough for common (80%) use cases. 

You can make extensions to the standard 
with "x-" mechanism in order to fulfill 
any industry specific needs. 

A suggestive example below 

SLA:
  declarative:
    - x-dimension: custom
      displaytitle:
        - en: Custom SLA
      objective: 99
      unit: percent
    - dimension: responseTime
      objective: 200
      unit: milliseconds
```

The SLA object is general in nature and should be enough for common (80%) use cases. Note that you can make extensions to the standard with "x-" mechanism in order to fulfill any industry specific needs. The ["Specification extensions"](#specification-extensions) section provides details on how to use this feature.


## SLA can be defined with 11 standardized dimensions with decoupled Everything as Code monitoring

> Example of SLA component usage:

```yml

SLA:
  declarative:
    - dimension: uptime
      displaytitle:
        - en: Uptime
      objective: 99
      unit: percent
    - dimension: responseTime
      objective: 200
      unit: milliseconds

```

| <div style="width:150px">SLA Dimension</div>   | Description | 
|---|---|
| **latency** | minimal amount of time before getting any response. |
| **uptime** | Uptime is a measure of system reliability, expressed as the percentage of time a machine, typically a computer, has been working and available. See more https://uptime.is/. |
| **responseTime** | amount of time to process external request. |
| **errorRate** | Maximum tolerated errors in data, percentage. |
| **endOfSupport** | The date at which your product will not have support anymore. |
| **endOfLife** | The date at which your product will not be available anymore. No support, no access. |
| **updateFrequency** | how often data is updates. |
| **timeToDetect** | How fast can you detect a problem? |
| **timeToNotify** | Once you see a problem, how much time do you need to notify your users? |
| **timeToRepair** | How long do you need to fix the issue once it is detected? |
| **emailResponseTime** | How long do you need to respond to email support requests? |

No mandatory attributes at the moment. Optional attributes are listed in own table and an example is given in the right column. 

## Optional attributes and elements

> Example of SLA component usage:

```yml

SLA:
  declarative:
    - dimension: uptime
      displaytitle:
        - en: Uptime
      objective: 99
      unit: percent
    - dimension: responseTime
      objective: 200
      unit: milliseconds
    - dimension: updateFrequency
      objective: 30
      unit: minutes
    - dimension: errorRate
      objective: 0.1
      unit: percent
    - dimension: endOfSupport
      objective: 01/01/2025
      unit: date
    - dimension: endOfLife
      objective: 01/03/2025
      unit: date
  executable:
    - dimension: uptime
      type: prometheus
      reference: 'https://prometheus.io/docs/prometheus/latest/querying/basics/'
      spec: |-
        avg_over_time(
          (
            sum without() (up{job="prometheus"})
              or
            (0 * sum_over_time(up{job="prometheus"}[7d]))
          )[7d:5m]
        )   
    - dimension: responseTime
      type: prometheus
      reference: 'https://prometheus.io/docs/prometheus/latest/querying/basics/'
      spec: |-
        rate(http_server_requests_seconds_sum[$__rate_interval]) /
        rate(http_server_requests_seconds_count[$__rate_interval])
  support:
    phoneNumber: '+971508976456'
    phoneServiceHours: Mon-Fri 8am-4pm (GMT)
    email: support@opendataproducts.org
    emailServiceHours: Mon-Fri 8am-4pm (GMT)
    documentationURL: ''

```



| <div style="width:150px">Element name</div>   | Type  | Options  | Description  |
|---|---|---|---|
| **SLA** | element | - | Binds the SLA related elements and attributes together |
| **declarative** | element | - | Grouping element which collects together SLA dimensions target level (objectives), name to display in UI in wanted languages, measuring unit used, and dimension name (one of standardized options). |
| **dimension** | attribute | string, one of: *latency, uptime, responseTime, errorRate, endOfSupport, endOfLife, updateFrequency, timeToDetect, timeToNotify, timeToRepair, emailResponseTime* | Defines the SLA dimension.   |
| **unit** | attribute  | Options for *unit* are: milliseconds, seconds, minutes, days, weeks, months, years, never, date, null. <br/><br/>  | Name of the quality attribute indicating the timely interval. If date is given, format is dd/mm/yyyy |
| **executable** | element | - | Grouping element which collects together SLA monitoring. You can define the monitoring patterns as code under this element for the above mentioned SLA dimensions. In other words, contains the monitoring (computational "as code") structure to validate target state for the selected SLA dimension. The actual as code part is added with _spec_ element. |
| **displayTitle** | array | - | Dimension title to be shown is various UIs. Keep it short and sweet. |
| **en** | attribute | [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) defined 2-letter codes | This element binds together other product attributes and expresses the langugage used. In the example this is "en", which indicates that product details are in English. If you would like to use French details, then name the element "fr". The naming of this element follows options (language codes) listed in [ISO 639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes) standard. <br/><br/> You can have product details in multiple languages simply by adding similar sets like the example - just change the binding element name to matching language code. <br/><br/> The pattern to implement multilanguage support for data products was adopted from de facto UI translation practices. The attributes inside this element are commonly rendered in the UI for the consumer and providing a simple way to implement that was the driving reasoning. See for example  [JSON - Multi Language](https://simplelocalize.io/docs/file-formats/multi-language-json/) |
| **type** | attribute | string | monitoring system name name such as Prometheus. The system used must support as code approach to monitor SLA. |
| **spec** | element | YAML/URL/string | The content the as code part for SLA monitoring. Content is intended to be in a form that can be injected as is to _type_ defined monitoring system. Content depends of the system used and reference attribute is expected to provide more information. <br/><br/> **Note!** By default the rules must be provide as valid String or YAML. If YAML is used, it must be either as inline element (YAML) or as valid URL (filesystem or online) pointing to valid YAML or string content file. |
| **reference** | URL | Valid URL | Provide URL for the reference documentation regarding used monitoring system. |
| **support** | element | - | Support element describes how the customer can reach for help in case of difficulties in usage, billing, or otherwise. |
| **phoneNumber** | string | valid phone number | The support phone number. Use [E.164](https://www.itu.int/rec/T-REC-E.164/en)  |
| **phoneServiceHours** | string | - | Describes the service hours company provides. Contains information often in week level eg Mon-Fri at 8am - 4pm. |
| **email** | string | valid email address | Email information for support requests. Use [RFC2822](https://datatracker.ietf.org/doc/html/rfc2822) |
| **emailServiceHours** | string | - | Describes the email service hours company provides. Contains information often in week level eg Mon-Fri at 8am - 4pm. |
| **documentationURL** | URL | Valid URL | URL to documentation | 


If you see something missing, described inaccurately or plain wrong, or you want to comment the specification, [raise an issue in Github](https://github.com/Open-Data-Product-Initiative/dev/issues)
