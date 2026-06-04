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

---

## Decision 003: Model BPMN Participants as Business Roles

### Context

The analyzed organization is currently operated by a single person who performs all operational activities, including order processing, payment verification, packaging, shipment preparation, and customer communication.

However, the purpose of the BPMN diagram is to describe the business process rather than the current organizational structure.

### Decision

BPMN participants are modeled as business roles (Sales, Finance, Warehouse) instead of specific individuals.

### Consequences

* The process remains understandable regardless of the current team size.
* The model can support future organizational growth without requiring major changes.
* Responsibilities are clearly separated at the process level.
* The BPMN diagram reflects business capabilities rather than individual staffing arrangements.

