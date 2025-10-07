# ODPS 4.0 → 4.1 Migration Guide

Version 4.1 is a **minor, fully backward-compatible update** to the Open Data Product Specification.  
Existing 4.0 YAML files remain valid without modification.

```yaml
product:
  productStrategy:
    objectives:
    strategicAlignment:
    contributesToKPI:
    productKPIs:
    relatedKPIs:
```

### 1. New `productStrategy` object
A new top-level object under `product` introduces the ability to connect data products to business outcomes.

**Purpose:**  
- Express business **objectives** and **strategic alignment**  
- Define measurable **product KPIs**  
- Link to higher-level **business KPIs (OKRs)**  

**Location in schema on the left example**

See the [ODPS 4.1 schema](https://opendataproducts.org/v4.1rc/schema) for full JSON/YAML definitions.


### Backward Compatibility

| ODPS 4.0 Element | ODPS 4.1 Change | Action Required |
|------------------|-----------------|----------------|
| All existing objects (`details`, `SLA`, `dataQuality`, etc.) | No change | None |
| `productStrategy` | New optional block | Add only if you want to link products to KPIs/OKRs |

No breaking or renaming occurred.  
Tooling built on 4.0 will continue to work.

### How to Extend an Existing 4.0 File

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

Add the following minimal block under `product:`  


### Summary

| Topic | 4.0 | 4.1 |
|--------|-----|-----|
| Specification type | Modular YAML schema | Same |
| New object | — | `productStrategy` |
| Business linkage | External | Built-in |
| Compatibility | — | 100 % backward-compatible |



### Next Steps
- Update internal templates or tools if you want to capture KPI/OKR alignment.  
- No urgent migration is required for existing 4.0 files.  

