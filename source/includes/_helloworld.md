# Hello world example

You'll find a complete machine-readbale example of a data product from the right column. It is imaginary data product *Pets of the year* which contains derived data about the most common pets in the world. The product has 4 pricing plans which are mostly based on recurring subscription model. Note! Not all voluntary attributes are used in the example and multilingualism has not been fully applied.

> Example of complete working Data Product specification instance:

```yml

---
schema: https://raw.githubusercontent.com/Open-Data-Product-Initiative/open-data-product-spec-dev/ddbc069196a664d0e28a0f3dc7c1c7fb49b64591/source/schema/odps-dev-json-schema.json
version: dev
product:
  en:
    name: Pets of the year
    productID: 123456are
    valueProposition: Design a customised petstore using a data product that describes
      pets with their habits, preferences and characteristics.
    description: This is an example of a Petstore product.
    productSeries: Lovely pets data products
    visibility: private
    status: draft
    version: '0.1'
    categories:
    - pets
    standards:
    - ISO 24631-6
    tags:
    - pet
    brandSlogan: Passion for the data monetization
    type: derived data
    logoURL: https://data-product-business.github.io/open-data-product-spec/images/logo-dps-ebd5a97d.png
    OutputFileFormats:
    - json
    - xml
    - csv
    - zip
    useCases:
    - useCase:
        useCaseTitle: Build attractive and lucrative petstore!
        useCaseDescription: Use case description how succesfull petstore chain was
          established in Abu Dhabi
        useCaseURL: https://marketplace.com/usecase1
  recommendedDataProducts:
  - https://marketplace.com/dataproduct.json, https://marketplace.com/dataproduct-another.json
  pricingPlans:
    en:
    - name: Premium subscription 1 year
      priceCurrency: EUR
      price: '50.00'
      billingDuration: year
      unit: recurring
      maxTransactionQuantity: unlimited
      offering:
        - item 1
    - name: Premium Package Monthly
      priceCurrency: EUR
      price: '5.00'
      billingDuration: month
      unit: recurring
      maxTransactionQuantity: 10000
      offering:
        - item 1
    - name: Freemium Package
      priceCurrency: EUR
      price: '0.00'
      billingDuration: month
      unit: recurring
      maxTransactionQuantity: 1000
      offering:
        - item 1
    - name: Revenue sharing
      priceCurrency: percentage
      price: '5.50'
      billingDuration: month
      unit: revenue-sharing
      maxTransactionQuantity: 20000
      offering:
        - item 1
  dataOps:
    data:
      schemaLocationURL: http://http://192.168.10.1/schemas/2016/petshopML-2.3/schema/petstore.xsd

    lineage:
      dataLineageTool: Collibra
      dataLineageOutput: http://192.168.10.1/lineage.json

    infrastructure:
      platform: Azure
      region: West US 2 (Washington)
      storageTechnology: Azure SQL
      storageType: sql
      containerTool: helm

    build:
      format: yaml
      hashType: SHA-2
      checksum: 7b7444ab8f5832e9ae8f54834782af995d0a83b4a1d77a75833eda7e19b4c921
      signatureType: JWK
      scriptURL: http://192.168.10.1/rundatapipeline.yml
      deploymentDocumentationURL: http://192.168.10.1/datapipeline

  dataAccess:
    type: API
    authenticationMethod: OAuth
    specification: OAS
    format: JSON
    documentationURL: https://swagger.com/petstore.json

  SLA:
  - dimension: latency
    displaytitle:
      - en: Latency
    objective: 100
    unit: milliseconds
    monitoring:
      type: prometheus
      reference: https://prometheus.io/docs/prometheus/latest/querying/basics/ 
      spec:  
        myTimer.observeDuration();

  - dimension: uptime
    displaytitle:
      - en: Uptime
    objective: 99
    unit: percent
    
  - dimension: responseTime
    objective: 200
    unit: milliseconds
    monitoring:
      type: prometheus
      reference: https://prometheus.io/docs/prometheus/latest/querying/basics/ 
      spec:  
       rate(http_server_requests_seconds_sum[$__rate_interval]) / rate(http_server_requests_seconds_count[$__rate_interval])

  - dimension: errorRate
    objective: 0.1
    unit: percent
  
  - dimension: endOfSupport
    objective: 01/01/2025 # dd/mm/yyyy
    unit: date

  - dimension: endOfLife
    objective: 01/03/2025 # dd/mm/yyyy
    unit: date

  - dimension: updateFrequency
    objective: 7
    unit: days

  - dimension: timeToDetect
    objective: 60
    unit: minutes

  - dimension: timeToNotify
    objective: 120
    unit: minutes

  - dimension: timeToRepair
    objective: 24
    unit: hours

  - dimension: emailResponseTime
    objective: 12
    unit: hours

  support:
      phoneNumber: '+971508976456'
      phoneServiceHours: 'Mon-Fri 8am-4pm (GMT)'
      email: support@opendataproducts.org
      emailServiceHours: 'Mon-Fri 8am-4pm (GMT)'
      documentationURL: ''
      
  dataQuality:
  - dimension: accuracy
    displaytitle:
    - en: Data Accuracy (percent)
    - fi: Datan virheettömyys (prosenttia)
    objective: 98
    unit: percentage
    monitoring:
      type: SodaCL 
      reference: https://docs.soda.io/soda-cl/soda-cl-overview.html
      spec:
        - require_unique(member_id) 
        - require_range(age_band, 18, 100)

  - dimension: completeness
    displaytitle:
    - en: Data Completeness
    objective: 99.9
    unit: percentage
    monitoring:
      type: SodaCL 
      reference: https://docs.soda.io/soda-cl/soda-cl-overview.html
      spec:
        - for each column:
            name: [member_id, gender, age_band]
            checks:
              - not null:
                  fail: when > 0.1% # Fail if more than 0.1% of records are null

  - dimension: consistency
    objective: 98
    unit: percentage

  - dimension: timeliness
    objective: 100
    unit: percentage

  - dimension: validity
    objective: 98
    unit: percentage

  - dimension: uniqueness
    objective: 100
    unit: percentage
  license:
    scope:
      definition: The purpose of this license is to determine the terms and conditions
        applicable to the licensing of the data product, whereby Data Holder grants
        Data User the right to use the data.
      language: en-us
      restrictions: Data User agrees not to, directly or indirectly, participate in
        the unauthorized use, disclosure or conversion of any confidential information.
      geographicalArea:
      - EU
      - US
      permanent: false
      exclusive: false
      rights:
      - Reproduction
      - Display
      - Distribution
      - Adaptation
      - Reselling
      - Sublicensing
      - Transferring
    termination:
      terminationConditions: Cancellation before 30 days. After the expiry of the
        right of use, the product and its derivatives must be removed.
      continuityConditions: Expired license will automatically continued without written
        cancellation (termination) by Data Holder
    governance:
      ownership: Mindmote Oy, a company specializing in pet industry insights, owns
        the license to its proprietary data product 'Pets of the Year'.
      damages: During the term of license, except for the force majeure or the Data
        Holders reasons, Data User is required to follow strictly in accordance with
        the license. If Data User wants to terminate the license early, it needs to
        pay a certain amount of liquidated damages.
      confidentiality: Data User undertakes to maintain confidentiality as regards
        all information of a technical (such as, by way of a non-limiting example,
        drawings, tables, documentation, formulas and correspondence) and commercial
        nature (including contractual conditions, prices, payment conditions) gained
        during the performance of this license.
      applicableLaws: This license shall be interpreted, construed and enforced in
        accordance with the law of Finland, including Copyright Act 404/1961.
      warranties: Data Holder makes no warranties, express or implied, guarantees
        or conditions with respect to your use of the data product. To the extent
        permitted under local law, Data Holder disclaims all liability for any damages
        or losses, including direct, consequential, special, indirect, incidental
        or punitive, resulting from Data User use of the data product.
      audit: Data Holder will reasonably cooperate with Data Users by providing available
        additional information about the data product. Both parties will bear their
        own audit-related costs.
      forceMajeure: Both parties may suspend their contractual obligations when fulfillment
        becomes impossible or excessively costly due to unforeseeable events beyond
        their control, such as strikes, fires, wars, and other force majeure events.
  dataHolder:
    taxID: 12243434-12
    vatID: 12243434-12
    businessDomain: Data Product Business
    logoURL: https://mindmote.fi/logo.png
    description: Digital Economy services and tools
    URL: https://mindmote.fi
    telephone: "+358 45 232 2323"
    streetAddress: Koulukatu 1
    postalCode: '33100'
    addressRegion: Pirkanmaa
    addressLocality: Tampere
    addressCountry: Finland
    aggregateRating: ''
    ratingCount: 1245
    slogan: ''
    parentOrganization: ''


```
