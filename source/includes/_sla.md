# Data SLA

Data Service Level Agreement (SLA) **Object** contains attributes which define the desired and promised quality of the data product. 

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
      spec:  
        myTimer.observeDuration();

  uptime:
    unit: percentage
    value: 99
  responseTime:
    unit: milliseconds
    value: 200
  support:
    company:
      phoneNumber: ''
      phoneServiceHours: ''
      chatURL: ''
      chatServiceHours: ''
      chatResponseTime: ''
      email: support@opendataproducts.org
      emailServiceHours: ''
      emailResponseTime: ''
      documentationURL: ''
      guidesURL: ''
    community:
      stackoverflowURL: ''
      forumURL: ''
      slackURL: ''
      twitterURL: ''


```

```json

{
    "dataQuality": [
        {
            "dimension": "accuracy",
            "objective": 98,
            "unit": "percentage",
            "monitoring": {
                "type": "SodaCL",
                "spec": [
                    "require_unique(member_id)",
                    "require_range(age_band, 18, 100)"
                ]
            }
        },
        {
            "dimension": "completeness",
            "objective": 98,
            "unit": "percentage",
            "monitoring": {
                "type": "SodaCL",
                "spec": [
                    {
                        "for each column": {
                            "name": [
                                "member_id",
                                "gender",
                                "age_band"
                            ],
                            "checks": [
                                {
                                    "not null": {
                                        "fail": "when > 2%"
                                    }
                                }
                            ]
                        }
                    }
                ]
            }
        },
        {
            "dimension": "consistency",
            "objective": 98,
            "unit": "percentage"
        },
        {
            "dimension": "timeliness",
            "objective": 100,
            "unit": "percentage"
        },
        {
            "dimension": "validity",
            "objective": 98,
            "unit": "percentage"
        },
        {
            "dimension": "uniqueness",
            "objective": 100,
            "unit": "percentage"
        }
    ]
}



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
