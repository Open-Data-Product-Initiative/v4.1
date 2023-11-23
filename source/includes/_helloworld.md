# Hello world example

You'll find a complete machine-readbale example of a data product from the right column. It is imaginary data product *Pets of the year* which contains derived data about the most common pets in the world. The product has 4 pricing plans which are mostly based on recurring subscription model. Note! Not all voluntary attributes are used in the example and multilingualism has not been fully applied.

> Example of complete working Data Product specification instance:

```javascript
{
    "$schema":"https://raw.githubusercontent.com/Open-Data-Product-Initiative/open-data-product-spec-dev/ddbc069196a664d0e28a0f3dc7c1c7fb49b64591/source/schema/odps-dev-json-schema.json",
    "$version":"dev",
    "product":{
        "en":{
            "name":"Pets of the year",
            "productID":"123456are",
            "valueProposition":"Design a customised petstore using a data product that describes pets with their habits, preferences and characteristics.",
            "description":"This is an example of a Petstore product.",
            "productSeries":"Lovely pets data products",
            "visibility":"private",
            "status":"draft",
            "version":"0.1",
            "categories":[
                "pets"
            ],
            "standards":[
                "ISO 24631-6"
            ],
            "tags":[
                "pet"
            ],
            "brandSlogan":"Passion for the data monetization",
            "type":"derived data",
            "logoURL":"https://data-product-business.github.io/open-data-product-spec/images/logo-dps-ebd5a97d.png",
            "OutputFileFormats":[
                "json",
                "xml",
                "csv",
                "zip"
            ],
            "useCases":[
                {
                    "useCase":{
                        "useCaseTitle":"Build attractive and lucrative petstore!",
                        "useCaseDescription":"Use case description how succesfull petstore chain was established in Abu Dhabi",
                        "useCaseURL":"https://marketplace.com/usecase1"
                    }
                }
            ]
        },
        "recommendedDataProducts":[
            "https://marketplace.com/dataproduct.json, https://marketplace.com/dataproduct-another.json"
        ],
        "pricingPlans":{
            "en":[
                {
                    "name":"Premium subscription 1 year",
                    "priceCurrency":"EUR",
                    "price":"50.00",
                    "billingDuration":"year",
                    "unit":"recurring",
                    "maxTransactionQuantity":"unlimited"
                },
                {
                    "name":"Premium Package Monthly",
                    "priceCurrency":"EUR",
                    "price":"5.00",
                    "billingDuration":"month",
                    "unit":"recurring",
                    "maxTransactionQuantity":10000
                },
                {
                    "name":"Freemium Package",
                    "priceCurrency":"EUR",
                    "price":"0.00",
                    "billingDuration":"month",
                    "unit":"recurring",
                    "maxTransactionQuantity":1000
                },
                {
                    "name":"Revenue sharing",
                    "priceCurrency":"percentage",
                    "price":"5.50",
                    "billingDuration":"month",
                    "unit":"revenue-sharing",
                    "maxTransactionQuantity":20000
                }
            ]
        },
        "dataOps":{
            "infrastructure":{
                "platform":"Azure",
                "storageTechnology":"Azure SQL",
                "storageType":"sql",
                "containerTool":"helm",
                "format":"yaml",
                "schemaLocationURL":"http://http://192.168.10.1/schemas/2016/petshopML-2.3/schema/petstore.xsd",
                "scriptURL":"http://192.168.10.1/rundatapipeline.yml",
                "deploymentDocumentationURL":"http://192.168.10.1/datapipeline",
                "dataLineageTool":"Collibra",
                "dataLineageOutput":"http://192.168.10.1/lineage.json",
                "hashType":"SHA-2",
                "checksum":"7b7444ab8f5832e9ae8f54834782af995d0a83b4a1d77a75833eda7e19b4c921"
            }
        },
        "dataAccess":{
            "type":"API",
            "authenticationMethod":"OAuth",
            "specification":"OAS",
            "format":"JSON",
            "documentationURL":"https://swagger.com/petstore.json"
        },
        "SLA":{
            "updateFrequency":{
                "unit":"hours",
                "value":1
            },
            "uptime":{
                "unit":"percentage",
                "value":99
            },
            "responseTime":{
                "unit":"milliseconds",
                "value":200
            },
            "nullValues":{
                "unit":"percentage",
                "value": 0.01
            },
            "support":{
                "company":{
                    "phoneNumber":"",
                    "phoneServiceHours":"",
                    "chatURL":"",
                    "chatServiceHours":"",
                    "chatResponseTime":"",
                    "email":"",
                    "emailServiceHours":"",
                    "emailResponseTime":"",
                    "documentationURL":"",
                    "guidesURL":""
                },
                "community":{
                    "stackoverflowURL":"",
                    "forumURL":"",
                    "slackURL":"",
                    "twitterURL":""
                }
            },
            "observability":{
                "logsURL":"https://logs.com",
                "dashboardURL":"https://dashboard.com",
                "uptimeURL":"https://uptime.com"
            }
        },
        "dataQuality":{
            "accuracy":100,
            "completeness":100,
            "consistency":100,
            "timeliness":"high",
            "validity":100,
            "uniqueness":100,
            "dataQualityAssuranceMethods":"Data quality assurance suite of tools and methods include both data quality auditing (DQA) tools designed for use by external audit teams and routine data quality assessment (RDQA) tools designed for capacity building and self-assessment.",
            "dataQualityMonitoring":"Soda",
            "monitoringScriptURL":"http://192.168.10.1/soda-petshop.py"
        },
        "dataGovernance":{
            "versionControlSystem":"Git",
            "versionRepositoryURL":"https://example.com/git-repo",
            "accessPermissions":{
                "permissionLevels":{
                    "level1":{
                        "read":true,
                        "write":false
                    },
                    "level2":{
                        "read":false,
                        "write":true
                    },
                    "level3":{
                        "read":true,
                        "write":true
                    }
                },
                "userGroups":{
                    "groupA":{
                        "levels":[
                            "level1"
                        ],
                        "description":""
                    },
                    "groupB":{
                        "levels":[
                            "level2"
                        ],
                        "description":""
                    },
                    "groupC":{
                        "levels":[
                            "level3"
                        ],
                        "description":""
                    }
                },
                "dataPrivacy":{
                    "containsPersonalData":true,
                    "applicablePrivacyLaws":[
                        "General Data Protection Regulation",
                        "Personal Information Protection and Electronic Documents Act (PIPEDA)",
                        "California Consumer Privacy Act (CCPA)"
                    ],
                    "dpaURL":"http://192.168.10.1/dpaconditions"
                },
                "dataSecurity":{
                    "encryption":"Data in transit is encrypted using the TLS 1.2 protocol with AES-256 encryption. Data at rest is encrypted using industry-standard AES-256 encryption algorithms.",
                    "authentication":"Users are initially authenticated using OAuth 2.0, where they grant access to their data or resources, without the need for a username and password combination. While multi-factor authentication (MFA) is not currently in use, it is under consideration for future implementation to enhance security.",
                    "vulnerabilities":"Security vulnerabilities are identified through regular automated scans and user-reported issues. A dedicated security team reviews and addresses these vulnerabilities. We have a vulnerability management process in place.",
                    "securityCertificatesAndAudits":"Our data product has undergone an annual security audit by a third-party firm, and we hold a SOC 2 Type II certification. The current certification is valid until December 31, 2024.",
                    "resilience":"In case of data breaches, we have a disaster recovery plan that includes data backups with daily snapshots. DDoS attacks are mitigated through a combination of traffic filtering and load balancing.",
                    "monitoring":"Log data is securely stored in an isolated environment with restricted access. We use real-time monitoring tools to detect anomalies, and automated alerts are triggered for any suspicious activities.",
                    "updates":"Security vulnerabilities are patched within 48 hours of discovery. Users are notified of security updates through email, and a dedicated changelog is maintained on our website."
                },
                "compliance":{
                    "confidentiality":"Ensuring data privacy and information security in accordance with relevant regulations and best practices.",
                    "regulations":"Access needs to be monitored to ensure compliance with data privacy and security regulations.",
                    "training":"Users need to receive training on data access policies and security best practices.",
                    "guidelines":"The data governance practices and guidelines are defined and followed to maintain data integrity and security.",
                    "audits":"We annually undergo external security audits by a third-party cybersecurity firm, with last year's audit confirming our data product's compliance and SOC 2 Type II certification validity until the end of 2024, ensuring robust security."
                }
            }
        },
        "license":{
            "scope":{
                "definition":"The purpose of this license is to determine the terms and conditions applicable to the licensing of the data product, whereby Data Holder grants Data User the right to use the data.",
                "language":"en-us",
                "restrictions":"Data User agrees not to, directly or indirectly, participate in the unauthorized use, disclosure or conversion of any confidential information.",
                "geographicalArea":[
                    "EU",
                    "US"
                ],
                "permanent":false,
                "exclusive":false,
                "rights":[
                    "Reproduction",
                    "Display",
                    "Distribution",
                    "Adaptation",
                    "Reselling",
                    "Sublicensing",
                    "Transferring"
                ]
            },
            "termination":{
                "terminationConditions":"Cancellation before 30 days. After the expiry of the right of use, the product and its derivatives must be removed.",
                "continuityConditions":"Expired license will automatically continued without written cancellation (termination) by Data Holder"
            },
            "governance":{
            "ownership":"Mindmote Oy, a company specializing in pet industry insights, owns the license to its proprietary data product 'Pets of the Year'.",
            "damages":"During the term of license, except for the force majeure or the Data Holders reasons, Data User is required to follow strictly in accordance with the license. If Data User wants to terminate the license early, it needs to pay a certain amount of liquidated damages.",
            "confidentiality":"Data User undertakes to maintain confidentiality as regards all information of a technical (such as, by way of a non-limiting example, drawings, tables, documentation, formulas and correspondence) and commercial nature (including contractual conditions, prices, payment conditions) gained during the performance of this license.",
            "applicableLaws":"This license shall be interpreted, construed and enforced in accordance with the law of Finland, including Copyright Act 404/1961.",
            "warranties":"Data Holder makes no warranties, express or implied, guarantees or conditions with respect to your use of the data product. To the extent permitted under local law, Data Holder disclaims all liability for any damages or losses, including direct, consequential, special, indirect, incidental or punitive, resulting from Data User use of the data product.",
            "audit":"Data Holder will reasonably cooperate with Data Users by providing available additional information about the data product. Both parties will bear their own audit-related costs.",
            "forceMajeure":"Both parties may suspend their contractual obligations when fulfillment becomes impossible or excessively costly due to unforeseeable events beyond their control, such as strikes, fires, wars, and other force majeure events."
        }
    },
        "dataHolder":{
            "taxID":"12243434-12",
            "vatID":"12243434-12",
            "businessDomain":"Data Product Business",
            "logoURL":"https://mindmote.fi/logo.png",
            "description":"Digital Economy services and tools",
            "URL":"https://mindmote.fi",
            "telephone":"+358 45 232 2323",
            "streetAddress":"Koulukatu 1",
            "postalCode":"33100",
            "addressRegion":"Pirkanmaa",
            "addressLocality":"Tampere",
            "addressCountry":"Finland",
            "aggregateRating":"",
            "ratingCount":1245,
            "slogan":"",
            "parentOrganization":""
        }
    }
}
```
