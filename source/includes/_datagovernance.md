# Data Governance

The Data Governance **OBJECT** pertains to the structured definition of policies, rules, and permissions that govern the management and utilization of data within an IT system or data product

> Example of Data Governance component usage:

```javascript
  
"dataGovernance": {
  "confidentiality": "Ensuring data privacy and information security in accordance with relevant regulations and best practices.",
  "versionControlSystem": "Git",
  "versionRepositoryURL": "https://example.com/git-repo",
  "accessPermissions": {
    "usersGroups": ["groupA", "groupB", "groupC"],
    "permissionLevels": {
      "level1": {
        "read": true,
        "write": false
      },
      "level2": {
        "read": false,
        "write": true
      },
      "level3": {
        "read": true,
        "write": true
      }
    },
    "userRights": {
      "groupA": {
        "level1": true,
        "level2": false,
        "level3": true,
        "description":""
      },
      "groupB": {
        "level1": true,
        "level2": false,
        "level3": false,
        "description":""
      },
      "groupC": {
        "level1": false,
        "level2": true,
        "level3": true,
        "description":""
      }
    },
    "compliance": {
      "regulations": "Access needs to be monitored to ensure compliance with data privacy and security regulations.",
      "training": "Users need to receive training on data access policies and security best practices.",
      "guidelines": "The data governance practices and guidelines are defined and followed to maintain data integrity and security."
    }
  }
}  
```
| <div style="width:150px">Element name</div>   | Type  | Options  | Description  |
|---|---|---|---|
| dataGovernance | element | - | Structured definition of policies, rules, and permissions that govern the management and utilization of data within an IT system or data product. |
| confidentiality | string | any | Ensuring data privacy and information security in accordance with relevant regulations and best practices.|
| versionControlSystem | string | any | A version control system (VCS) is a software tool that tracks and manages changes to files, enabling collaboration and providing a history of revisions. Examples: Git, Mercurial, Bazaar. |
| versionRepositoryURL | URL| Valid URL | The URL of the version repository, such as Git repository. |
| accessPermissions | element | - | Access permissions refer to the rights and restrictions that determine who can view, edit, or perform specific actions on data product. |
| permissionLevels| array | - | Comma separates array of permission levels and boolean values. |
| userRights| array | - | Comma separates array of user rights and boolean values. |
| compiliance| element | -  | Compliance refers to the adherence to established rules, regulations, and standards, ensuring that actions and practices align with legal and industry requirements, particularly in the context of data privacy and security. |
| regulations | string | any | Requirements for monitoring access to ensure compliance with data privacy and security regulations.|
| guidelines | string | any | Data governance practices and guidelines defined and followed to maintain data integrity and security.|
