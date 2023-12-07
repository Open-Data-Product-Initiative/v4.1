# Example with mandatory-only elements

Example data product with just the mandatory elements and attributes. 

> Example of mandatory-only elements and attributes Data Product specification instance:

```javascript
{
    "$schema":"https://raw.githubusercontent.com/Open-Data-Product-Initiative/open-data-product-spec-dev/ddbc069196a664d0e28a0f3dc7c1c7fb49b64591/source/schema/odps-dev-json-schema.json",
    "$version":"dev",
    "product":{
        "en":{
            "name":"Pets of the year",
            "productID":"123456are",
            "visibility":"private",
            "status":"draft",
            "type":"derived data"
        },
        "pricingPlans":{
            "en":[
                {
                    "name":"Freemium Package",
                    "priceCurrency":"EUR",
                    "price":"0.00",
                    "billingDuration":"month",
                    "unit":"recurring",
                    "maxTransactionQuantity":1000
                }
            ]
        },
        "dataHolder":{
            "legalName":"MindMote Oy",
            "businessId":"12243434-12",
            "email":"contact@mindmote.fi"
        }
    }
}
```
