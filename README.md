<p align="center">
  <img src="https://opendataproducts.org/img/profile.png" alt="Open Data Product Specification" width="300">
</p>

# Open Data Product Specification (ODPS)

The **Open Data Product Specification (ODPS)** is a vendor-neutral, open-source, machine-readable metadata model for data products.  
It defines the key **objects, attributes, and relationships** that describe digital data products — enabling a consistent, interoperable way to manage, share, and monetize them.

Built on established standards such as **schema.org**, ODPS applies modern product thinking to data.  
It is designed for **both open and commercial data products**, supporting interoperability, monetization, and AI-native automation across ecosystems.

---

## New in ODPS 4.1 — Connecting Data Products to Business Outcomes

Version 4.1 introduces the **`productStrategy`** object — a new addition that connects data products directly to measurable business goals.  

Data products can now declare:

- **Objectives** — the business intent or OKR objective the product supports.  
- **Product KPIs** — how success is measured at the product level.  
- **Business KPI (`contributesToKPI`)** — the higher-level outcome the product drives.  
- **Strategic Alignment** — optional references to corporate strategies or initiatives.

This makes ODPS 4.1 the **first open standard** to formalize the link between data products and business performance.  
It supports both **KPI** and **OKR** models, turning every YAML file into a living artifact of strategy execution — showing not just *what* a data product delivers, but *why* it matters.

**Example excerpt**

```yaml
productStrategy:
  objectives:
    - en: "Enable smarter marketing campaigns"
  contributesToKPI:
    id: "KPI-OUT-001"
    name: "Retail Revenue Uplift"
    unit: "percent"
    target: 5
    direction: increase
    timeframe: "2025-Q4"
  productKPIs:
    - id: "KPI-OUT-001-A"
      name: "Customer dataset usage"
      unit: "downloads"
      target: 4000
```

---

## Specification Aims

* Enable **interoperability** between organizations, data platforms, marketplaces, and tools.  
* Reduce metadata conversion friction and errors between systems.  
* Accelerate the **design, testing, and deployment** of data products.  
* Power **tool automation** and **DataOps** through a shared schema.  
* Bridge the gap between **technical outputs and business outcomes**.  

> **Note:** In “Open Data Product,” the word *open* refers to the openness of the **standard**, not to open-data licensing or access.

---

## Companies Using ODPS

ODPS is adopted by organizations and initiatives across public and private sectors — from **governments and data marketplaces** to **enterprises building AI-native data ecosystems**.

If your organization uses ODPS, we’d love to add your logo here.  
Please open a pull request or [contact the maintainers](https://github.com/Open-Data-Product-Initiative/open-data-product-spec/discussions).

---

## Questions? Need Help? Found a Bug?

If you’ve got questions about implementation, contributing, or special features,  
please start a thread in our [**Discussions** tab](https://github.com/Open-Data-Product-Initiative/open-data-product-spec/discussions).

Found a bug?  
Submit an [**issue**](https://github.com/Open-Data-Product-Initiative/open-data-product-spec/issues) or propose improvements with a pull request to the `dev` branch.

---

## Contributors

The **Open Data Product Specification** was originally created by  
**Jarkko Moilanen** and **Jussi Niilahti**.  

The project continues to be maintained and expanded under the  
**Open Data Product Initiative**, hosted by the **Linux Foundation** since 2024.

---
