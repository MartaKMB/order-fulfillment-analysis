# Order Fulfillment Analysis

A business process analysis project based on a real-world WooCommerce e-commerce store.

The goal of the project is to analyze the current order fulfillment process, identify operational bottlenecks, validate assumptions using operational data, and propose process improvements supported by process modeling and data analysis.

![AS-IS BPMN](./diagrams/as-is-bpmn.png)

The process was analyzed using BPMN, UML modeling techniques, WooCommerce operational data, and Python-based data extraction.

---

## Project Goals

* Model the current fulfillment process using BPMN and UML.
* Analyze shipment handling using WooCommerce data.
* Identify operational bottlenecks.
* Validate assumptions using operational data.
* Propose process improvements.
* Document decisions and assumptions.

---

## Highlights

* BPMN process modeling (AS-IS and TO-BE)
* UML Use Case Diagram
* UML Sequence Diagram
* WooCommerce REST API integration
* Python-based data extraction and aggregation
* Data-driven process analysis
* Process improvement recommendations
* Documentation using Markdown and ADR-style decisions

---

## Business Context

The analyzed store offers both physical and digital products.

Available payment methods:

* Przelewy24
* Traditional bank transfer

Available shipment methods:

* InPost Paczkomaty
* InPost Kurier
* Poczta Polska

The analysis focuses on the order fulfillment process from order placement to shipment dispatch.

---

## Modeling Techniques

The project uses multiple complementary analysis techniques.

| Technique            | Purpose                                                 |
| -------------------- | ------------------------------------------------------- |
| BPMN                 | Business process flow and responsibilities              |
| UML Use Case Diagram | Actors and system interactions                          |
| UML Sequence Diagram | Communication between participants and external systems |
| Data Analysis        | Validation of assumptions using operational data        |

---

## Repository Structure

```text
.
├── diagrams/
│   ├── as-is-bpmn.png
│   ├── use-case-diagram-uml.png
│   └── sequence-diagram-uml.png
│
├── docs/
│   ├── as-is.md
│   ├── metrics.md
│   ├── to-be.md
│   └── decisions.md
│
├── scripts/
│   ├── fetch-shipping-stats.py
│   └── generate-shipping-metrics.py
│
├── data/
│   └── .gitkeep
│
├── requirements.txt
└── README.md
```

---

## Documentation

### AS-IS Analysis

Description of the current fulfillment process, process participants, operational constraints, supporting metrics and process models.

See:

`docs/as-is.md`

### Metrics

Shipment method distribution based on WooCommerce order data.

See:

`docs/metrics.md`

### TO-BE Proposal

Recommended future-state process and proposed improvements.

See:

`docs/to-be.md`

### Decisions

Key project decisions, assumptions and modeling choices.

See:

`docs/decisions.md`

---

## Key Findings

The analysis identified that multiple shipment providers share a common operational workflow.

Operational activities related to Poczta Polska handling may introduce delays for InPost shipments despite the different characteristics of both delivery channels.

The analysis also showed that Poczta Polska remains a significant shipment channel and should not be removed solely based on operational inconvenience.

The proposed improvement separates shipment handling activities while preserving customer choice and existing business capabilities.

---

## Data Analysis

WooCommerce REST API is used to extract shipment data.

Shipment metrics are generated automatically using Python scripts.

Only aggregated metrics are included in the repository.

Raw order-level data is intentionally excluded from version control.

---

## Reproducing the Analysis

### Create a `.env` file

```env
WC_STORE_URL=
WC_CONSUMER_KEY=
WC_CONSUMER_SECRET=
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Fetch shipment data

```bash
python scripts/fetch-shipping-stats.py
```

### Generate metrics

```bash
python scripts/generate-shipping-metrics.py
```

---

## Data Privacy

Raw order-level data is not committed to the repository.

Only aggregated metrics and process documentation are published.

The repository is designed to demonstrate the analytical approach and findings without exposing customer or business-sensitive information.

---

## Disclaimer

This repository is intended for business process analysis, learning and portfolio purposes.

The analyzed process is based on a real e-commerce operation, but all published data has been aggregated to protect privacy.
