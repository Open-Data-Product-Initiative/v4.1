# Data Product Strategy

> Example of product strategy and KPIs usage:

```yml
version: "1.0"
product:
  productStrategy:
    objectives:
      - en: Reduce emergency response time
    kpis:
      coverage:
        name: Event Detection Coverage
        description: Percentage of city-reported events captured in real time
        objective: 95%
        unit: percentage

      time-to-insight:
        name: Average Time to Insight
        description: Median time between event occurrence and product update
        objective: < 60 seconds
        unit: seconds
    strategicAlignment:
      - en: Smart City Vision 2030
```
The `productStrategy` object captures the business intent behind a data product, enabling alignment between product specifications and organizational goals. It defines the objectives, success metrics (`KPIs`), and strategic alignment relevant to the product. This metadata can be used to trace value creation, measure performance, and communicate the product’s purpose to internal stakeholders, external consumers, and AI agents.

By embedding business logic directly into the product specification, `productStrateg`y helps ensure that data products are not only technically sound but also strategically impactful.

## Optional attributes and elements

| <div style="width:180px">Element name</div> | Type             | Options                  | Description                                                                 |
|--------------------------------------------|------------------|--------------------------|-----------------------------------------------------------------------------|
| **productStrategy**                        | object           | -                        | Top-level block that connects the data product to business goals and KPIs  |
| **objectives**             | array of objects | language-tagged strings  | Business objectives the product supports, written in natural language       |
| **kpis**                   | array            | `$ref` or inline object  | Key performance indicators that define success for this product             |
| **name**              | string           | -                        | Name of the KPI                                                             |
| **description**       | string           | -                        | Human-readable description of the KPI                                       |
| **unit**              | string           | e.g., `percentage`, `s`  | Unit of measurement for the KPI                                             |
| **objective**            | string/number    | -                        | Target value to be achieved                                                 |
| **strategicAlignment**     | array            | language-tagged strings  | Strategic initiatives, policies, or visions the product aligns with         |
 


Bring your ideas, questions, and use cases — [join the ODPS Discord](https://discord.gg/7KfnFxAc) and get involved!
