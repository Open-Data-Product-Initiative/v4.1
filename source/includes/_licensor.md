# Licensor

Licensor **Object** describes the Organization legal IPR owner of the data used. This might be occasionally the same as *Provider*. 

Mandatory attributes are listed in separate table and marked with **bolded names** and asterix **\***. Next to the mandatory attributes is an example. 

The same logic applies to the optional attributes as well. Optional attributes are listed in own table and an example is given in the right column. 

## Mandatory attributes and elements


> Example of Licensor Object mandatory attributes usage:

```javascript
   "Licensor":{
         "legalName":"MindMote Oy",
         "businessId":"12243434-12",
         "email":"contact@mindmote.fi"
      }
      
```

| <div style="width:150px">Element name</div>   | Type  | Options  | Description  |
|---|---|---|---|
| **legalName** **\*** | string  | text content, max length 256 chars  | The official name of the organization, e.g. the registered company name.  | 
|  **businessID** **\*** | string  | -  | The business identifier code of the company. Often this is given to the company by authorized public sector organization managing register of businesses.  |
| **email** **\*** | string | - | Email to be used in contacting the organization. |

If you see something missing, described inaccurately or plain wrong, or you want to comment the specification, [raise an issue in Github](https://github.com/Open-Data-Product-Initiative/open-data-product-spec-dev/issues)


## Optional attributes and elements

> Example of Licensor Object with some of the voluntary attributes:

```javascript
   "Provider":
      {
         "taxID":"12243434-12",
         "vatID":"12243434-12",
         "logoURL":"https://mindmote.fi/logo.png",
         "description":"Digital Economy services and tools",
         "URL":"https://mindmote.fi"
         "telephone":"+35845 0232 2323",
         "streetAddress":"Koulukatu 1",
         "postalCode":"33100",
         "addressRegion":"Pirkanmaa"
         "addressLocality":"Tampere",
         "addressCountry":"Finland",
         "aggregateRating":"",
         "ratingCount":1245,
         "slogan":"",
         "parentOrganization":""
      }
      
```

| <div style="width:150px">Element name</div>   | Type  | Options  | Description  |
|---|---|---|---|
| taxID | string  | - | The Tax / Fiscal ID of the organization or person, e.g. the TIN in the US or the CIF/NIF in Spain. |
| vatID | string | - | The Value-added Tax ID of the organization or person. |
| logoURL | URL | Valid URL | The URL pointing to organisation logo |
| description | string | Max length 512 chars | The introduction to the organization. Often contains information of what the organisation does and focuses on. |
| URL | URL | Valid URL | The URL of the organization's website  |
| telephone | string | - | The telephone number.  |
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
