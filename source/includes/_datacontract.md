# Data Contract

The optional `product.contract` object links an ODPS product to a formal data contract. Use either a
reference to an external contract, a compact contract identity with a URL, or an inline structured `spec`.
ODPS does not require a contract unless a publisher or profile adds that rule.

## External contract reference

```yml
contract:
  $ref: https://example.org/contracts/default.yaml
```

## Contract identity and URL

```yml
contract:
  id: 02323M123
  type: ODCS
  contractVersion: 2.2.2
  contractURL: https://example.org/contracts/02323M123
```

## Inline contract specification

```yml
contract:
  id: 02323M123
  type: ODCS
  contractVersion: 2.2.2
  spec:
    dataContractSpecification: odcs
    version: 1.0.0
```

| Element | Type | Description |
|---|---|---|
| `contract` | object | Optional contract link or inline description. |
| `$ref` | URI | Points to contract content in another file or online. |
| `id` | string | Contract identifier. |
| `type` | string | `ODCS` or `DCS`. |
| `contractVersion` | string | Version of the referenced contract standard. |
| `contractURL` | URI | Link to a contract in a management service. |
| `spec` | object | Inline structured contract content. |
