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

---

## Decision 004: Use Multiple Modeling Techniques

### Context

The project aims to analyze the order fulfillment process from both business and system perspectives.

A single modeling notation was not sufficient to describe all aspects of the analyzed process.

BPMN effectively models business workflows and responsibilities, but does not clearly illustrate system interactions or communication between participants.

### Decision

The process is modeled using multiple complementary techniques:

* BPMN for business process flow and responsibilities,
* UML Use Case Diagram for actor interactions,
* UML Sequence Diagram for communication between participants and external systems.

### Consequences

* The process can be analyzed from multiple perspectives.
* Business workflows and system interactions are documented separately.
* The documentation becomes easier to understand for both business and technical stakeholders.
* Additional diagrams increase documentation effort but provide a more complete view of the analyzed process.
