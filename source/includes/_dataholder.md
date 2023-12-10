# Data Holder

DataHolder **Object** describes the **Organization legally allowed to create, develop and publish data products.** 

*Data holder* means "a legal person, public body, international organisation, or a natural person who is not a data subject with respect to the specific data in question, which, in accordance with applicable Union or national law, has the right to grant access to or to share certain personal data or non-personal data." (Data Governance Act)

The *data holder* might not be the original IPR owner of the data used, but has rights operate with it. The contract or other agreement between Provider and possible data owner is not part of the standard as metadata or licence wise.

Mandatory attributes are listed in separate table and marked with **REQUIRED** text. Next to the mandatory attributes is an example. 

The same logic applies to the optional attributes as well. Optional attributes are listed in own table and an example is given in the right column. 

## Mandatory attributes and elements


> Example of Holder component mandatory attributes usage:

```yml

dataHolder:
  legalName: MindMote Oy
  businessId: 12243434-12
  email: contact@mindmote.fi
      
```

| <div style="width:150px">Element name</div>   | Type  | Options  | Description  |
|---|---|---|---|
| **dataHolder** | element | - | **REQUIRED** Binds the provider related business elements and attributes together |
| **legalName** | string  | text content, max length 256 chars  | **REQUIRED** The official name of the organization, e.g. the registered company name.  | 
|  **businessID**| string  | As defined in [RFC 5322](https://datatracker.ietf.org/doc/html/rfc5322)  | **REQUIRED** The business identifier code of the company. Often this is given to the company by authorized public sector organization managing register of businesses.  |
| **email** | string | - | **REQUIRED** Email to be used in contacting the organization. |

If you see something missing, described inaccurately or plain wrong, or you want to comment the specification, [raise an issue in Github](https://github.com/Open-Data-Product-Initiative/open-data-product-spec-dev/issues)


## Optional attributes and elements

> Example of Holder component with some of the voluntary attributes:

```yml

dataHolder:
  taxID: 12243434-12
  vatID: 12243434-12
  businessDomain: Product catalogs
  logoURL: https://mindmote.fi/logo.png
  description: Digital Economy services and tools
  URL: https://mindmote.fi
  telephone: "+35845 0232 2323"
  streetAddress: Koulukatu 1
  postalCode: 33100
  addressRegion: Pirkanmaa
  addressLocality: Tampere
  addressCountry: Finland
  aggregateRating: ''
  ratingCount: 1245
  slogan: ''
  parentOrganization: ''
      
```

| <div style="width:150px">Element name</div>   | Type  | Options  | Description  |
|---|---|---|---|
| taxID | string  | - | The Tax / Fiscal ID of the organization or person, e.g. the TIN in the US or the CIF/NIF in Spain. |
| vatID | string | - | The Value-added Tax ID of the organization or person. |
| businessDomain | string | - |  In a data mesh architecture, data (or data product) ownership and management are distributed across self-contained business domains. |
| logoURL | URL | Valid URL. See more from [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986). | The URL pointing to organisation logo. |
| description | string | Max length 512 chars | The introduction to the organization. Often contains information of what the organisation does and focuses on. |
| URL | URL | Valid URL. See more from [RFC 3986](https://datatracker.ietf.org/doc/html/rfc3986). | The URL of the organization's website.   |
| telephone | string | Valid telephone number | The telephone number. Use [E.164](https://www.itu.int/rec/T-REC-E.164-201011-I/en) standard.  |
| streetAddress | string | - | The street address. For example, 1600 Amphitheatre Pkwy.  |
| postalCode | string | - | The postal code. For example, 94043.  |
| addressRegion | string | - | The region in which the locality is, and which is in the country. For example, California or another appropriate first-level Administrative division |
| addressLocality | string | -  | The locality in which the street address is, and which is in the region. For example, Mountain View.  |
| addressCountry | string | two-letter ISO 3166-1 alpha-2 country code | The country.  |
| aggregateRating | string | - | The average rating based on multiple ratings or reviews. |
| ratingCount | integer | - | The amount of ratigns and reviews used in calculating the aggregateRating. |
| slogan | string | Max length 256 chars | The slogan of the organization. This is often related to showing the brand |
| parentOrganization | string | - | The larger organization that this organization is a subOrganization of, if any. |



If you see something missing, described inaccurately or plain wrong, or you want to comment the specification, [raise an issue in Github](https://github.com/Open-Data-Product-Initiative/open-data-product-spec-dev/issues)
