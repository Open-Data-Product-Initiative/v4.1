# Data Governance

The Data Governance **OBJECT** pertains to the structured definition of policies, rules, and permissions that govern the management and utilization of data product.

> Example of Data Governance component usage:

```javascript  
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
        "levels":["level1"],
        "description":""
      },  
      "groupB":{
        "levels":["level2"],
        "description":""
      },  
      "groupC":{
        "levels":["level3"],
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
}  
```
| <div style="width:150px">Element name</div>   | Type  | Options  | Description  |
|---|---|---|---|
| dataGovernance | element | - | Structured definition of policies, rules, and permissions that govern the management and utilization of data within an IT system or data product. |
| versionControlSystem | string | any | A version control system (VCS) is a software tool that tracks and manages changes to files, enabling collaboration and providing a history of revisions. Examples: Git, Mercurial, Bazaar. |
| versionRepositoryURL | URL| Valid URL | The URL of the version repository, such as Git repository. |
| accessPermissions | element | - | Access permissions refer to the rights and restrictions that determine who can view, edit, or perform specific actions on data product. |
| permissionLevels| array | - | Comma separates array of permission levels and boolean values. |
| userGroups| array | - | Comma separates array of group rights and boolean values. |
| dataPrivacy | element | - | Data privacy related attributes. |
| containsPersonalData | boolean | true/false | Data contains personal data. |
| applicablePrivacyLaws | string | any |  Applicable privacy laws. |
| dpaURL| URL| valid URL | The URL of the Data Processing Agreement (DPA). |
| dataSecurity | element | - | Information related to data product security. |
| encryption | string | any |  How data is encrypted both in transit and at rest. List encryption algorithms and protocols used. |
| authentication | string | any | How users are initially identified. |
| vulnerabilities | string | any | Process for identifying and responding to security vulnerabilities and gaps. |
| securityCertificatesAndAudits | string | any | Security certifications or audits the data product has undergone and provide their expiration dates if applicable. |
| resilience | string | any | How the data product recovers from incidents like data breaches or DDoS attacks. Includes details about backup and recovery plans. |
| monitoring | string | any | How log data from the data product is stored and monitored for security purposes. Processes for reporting and addressing anomalies. |
| updates | string | any | How security vulnerabilities are addressed and how security updates are managed. Describe the process for notifying users of updates. |
| compiliance| element | -  | Compliance refers to the adherence to established rules, regulations, and standards, ensuring that actions and practices align with legal and industry requirements, particularly in the context of data privacy and security. |
| confidentiality | string | any | Ensuring data privacy and information security in accordance with relevant regulations and best practices.|
| regulations | string | any | Requirements for monitoring access to ensure compliance with data privacy and security regulations.|
| guidelines | string | any | Data governance practices and guidelines defined and followed to maintain data integrity and security.|
| audits | string | any | Data Governance auditing terms.|

