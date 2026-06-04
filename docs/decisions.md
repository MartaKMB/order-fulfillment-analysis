# Project Decisions

## Decision 001: Keep BPMN labels in Polish

### Context

The analyzed process belongs to a Polish e-commerce company and is used by Polish-speaking business stakeholders.

### Decision

BPMN diagrams are modeled in Polish, while repository documentation is written in English.

### Consequences

- Business users can read the process diagram naturally.
- The repository remains accessible as a portfolio project.
- Some terms are intentionally not translated, such as InPost, Poczta Polska and Przelewy24.

---

## Decision 002: Do not commit raw order data

### Context

The analysis uses WooCommerce order data.

### Decision

Raw order-level CSV files are excluded from version control.

### Consequences

- Customer and order data remain private.
- Only aggregated metrics are published.
- Analysis can be reproduced locally using scripts.
