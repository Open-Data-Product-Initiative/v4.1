# Data Licensing

The data product may be exploited e.g. by licensing its use and exploitation to third parties. Machine-readable license as part of the specification is implemented for this purpose. It can be used to conclude various agreements regarding data protection, processing and intellectual property rights (IPR). Data can be protected by one or more intellectual property rights. Principle is that when a third party (Data User) exploits the data, it must have a license or other right from Data Holder to exploit to the data.

> Example of License Object usage:


```javascript  
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
	}
  
```
| <div style="width:150px">Element name</div>   | Type  | Options  | Description  |
|---|---|---|---|
| license | element | - |  Binds the licensing related elements and attributes together. |
| scope | element | - |  Extent, range, coverage, area or space of the license. |
| definition | string | text content, max length 512 chars  | Background and purpose of the license. |
| language | string | ISO 639-1 standard language codes | License language. |
| restrictions | string | text content, max length 512 chars  | Restrictions of the license. |
| geographicalArea | string |  ISO 3166-1 alpha-2 codes | License right restricted to the geographical area. |
| permanent | boolean | true/false |  License with no expiration date. |
| exclusive | boolean | true/false |  The exclusive license holder is given complete control over the use of the data product, and no other person or organization is allowed to use it during the term of the license agreement. |
| rights| array |  Options: Reproduction <i>(rights to reproduce)</i>, Display <i>(disclose data to others)</i>, Distribution <i>(right to distribute)</i>, Adaptation <i>(right for derivate work)</i>, Reselling <i>(right to resell)</i>, Transferring <i>(transferable data license)</i>, Sublicensing <i>(license grant may include a right to sublicense)</i>| Rights granted by the licence. The texts in brackets and <i>italic</i> are intended to describe rights. |
| termination | element | - | Licence termination and continuity related conditions. |
| terminationConditions | string | text content, max length 512 chars | Cancellation conditions of the license. |
| continuityConditions | string |  text content, max length 512 chars | Continuity conditions of the license. |
| governance | element | - | Governance is the approach taken to ensure that the agreed outcomes are being fulfilled. |
| ownership | string | text content, max length 512 chars | Data product licensing ownership. |
| audit | string | text content, max length 512 chars | License auditing terms. |
| warranties | string | text content, max length 512 chars | License warranties. |
| damages| string | text content, max length 512 chars | Damages refers to the sum of money (i.e. indemnifications) for a breach of some duty or violation of license right. |
| confidentiality | string | text content, max length 512 chars| Restrictions and requirements imposed on the Data User regarding e.g. the use and disclosure of the Data Holder's confidential information. |
| applicableLaws | string | text content, max length 512 chars | Applicable laws not covered in **applicaplePrivacyLaws**, i.e local acts, degrees or law. |
| forceMajeure | string | text content, max length 512 chars | Force majeure is a clause that is included in contracts to remove liability for unforeseeable and unavoidable catastrophes that interrupt the expected course of events and prevent participants from fulfilling obligations. These clauses generally cover both natural disasters and catastrophes created by humans. |
