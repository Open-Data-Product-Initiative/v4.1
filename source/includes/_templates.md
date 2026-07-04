# ODPS template family

ODPS can describe many kinds of data products. A full-schema example is useful for completeness, but it is too large as the first starting point for many teams. The ODPS template family gives users a smaller set of application skeletons that reuse the existing ODPS schema areas.

These templates are guidance patterns, not new schema objects. They do not add a mandatory `template` or `profile` field. Tools can still package them as starter files, replace the placeholders, validate the completed files with the normal ODPS schema, and extend them with additional ODPS components when needed.

Use the template that best matches the product intent. Do not use maturity labels such as Bronze, Silver, or Gold as template names, because they describe perceived quality instead of product purpose. Access methods such as API, SQL, file, MCP, GraphQL, gRPC, and AI should be modeled inside `product.dataAccess`; they are access patterns, not product templates.

The skeleton files are intentionally stored as separate YAML files so they can be copied, validated, versioned, and reused outside this documentation page. The skeletons use typed placeholders such as `{{string}}`, `{{integer}}`, `{{number or string}}`, `{{boolean}}`, and `{{enum: option | option}}` where users or tools must supply a value.

| Template | Use when | Main ODPS areas | Skeleton |
|---|---|---|---|
| **ODPS Product Profile** | Use this as the minimum starting point for any data product. It answers what the product is, who holds it, and what its status and visibility are. | `details`, `dataHolder` | [purpose-product-profile.yml](examples/Templates/purpose-product-profile.yml) |
| **ODPS Reusable Data Product** | Use this when the product packages reusable data for trusted consumption. It adds quality expectations to the product profile pattern. | `details`, `dataHolder`, `dataQuality`, `dataAccess` | [purpose-reusable-data-product.yml](examples/Templates/purpose-reusable-data-product.yml) |
| **ODPS Analytical Product** | Use this when the product delivers insight, reporting, indicators, or decision support. The template adds product strategy so the product can declare the business objective and KPIs it supports. | `details`, `dataHolder`, `productStrategy`, `dataQuality`, `SLA`, `dataAccess` | [purpose-analytical-product.yml](examples/Templates/purpose-analytical-product.yml) |
| **ODPS Agentic Product** | Use this when the product is consumed by AI agents, AI applications, workflows, automation, or machine-to-machine processes. It connects agentic use cases to strategy, quality, SLA, and named `dataAccess` methods such as MCP or API. | `details`, `useCases`, `productStrategy`, `dataAccess`, `SLA`, `dataQuality`, `contract`, `license` | [purpose-agentic-product.yml](examples/Templates/purpose-agentic-product.yml) |
| **ODPS Marketplace Product** | Use this when the product is offered under controlled, priced, licensed, contractual, or marketplace terms. The template connects pricing, license, contract, payment, quality, SLA, and access metadata. | `details`, `productStrategy`, `pricingPlans`, `license`, `contract`, `paymentGateways`, `dataAccess`, `SLA`, `dataQuality` | [purpose-marketplace-product.yml](examples/Templates/purpose-marketplace-product.yml) |

## Templates by description maturity

The following templates are organized by how complete the product description is at the time of use. They are not quality tiers. A product can start with a brief and later move to a definition or operating model as ownership, use cases, access, quality, and service expectations become known.

| Template | Use when | Main ODPS areas | Skeleton |
|---|---|---|---|
| **ODPS Product Brief** | Use this when only the basic identity, value proposition, lifecycle state, and product type are known. | `details` | [maturity-product-brief.yml](examples/Templates/maturity-product-brief.yml) |
| **ODPS Product Definition** | Use this when the product owner, business context, categories, tags, and use cases are known, but operational access and service terms are not yet complete. | `details`, `dataHolder`, `useCases` | [maturity-product-definition.yml](examples/Templates/maturity-product-definition.yml) |
| **ODPS Product Operating Model** | Use this when the product has known operational access, quality expectations, SLA expectations, and support metadata. | `details`, `dataHolder`, `dataAccess`, `dataQuality`, `SLA` | [maturity-product-operating-model.yml](examples/Templates/maturity-product-operating-model.yml) |
