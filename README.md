# Order Fulfillment Analysis

A process analysis project based on a real-world WooCommerce e-commerce store.

The goal of the project is to analyze the current order fulfillment process, identify operational bottlenecks, and propose process improvements supported by business process modeling and data analysis.

![AS-IS BPMN](/diagrams/as-is-bpmn.png)

---

## Project Goals

* Model the current fulfillment process using BPMN.
* Analyze shipment handling using WooCommerce data.
* Identify operational bottlenecks.
* Propose process improvements.
* Document decisions and assumptions.

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

## Repository Structure

```text
.
├── diagrams/
│   └── as-is-bpmn.png
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

### AS-IS Process

Description of the current fulfillment process.

See:

`docs/as-is.md`

### Metrics

Shipment method distribution based on WooCommerce order data.

See:

`docs/metrics.md`

### TO-BE Process

Proposed process improvements.

See:

`docs/to-be.md`

### Decisions

Key project decisions and assumptions.

See:

`docs/decisions.md`

---

## Data Analysis

WooCommerce REST API is used to extract shipment data.

Only aggregated metrics are included in the repository.

Raw order-level data is intentionally excluded from version control.

---

## Reproducing the Analysis

Create a `.env` file:

```env
WC_STORE_URL=
WC_CONSUMER_KEY=
WC_CONSUMER_SECRET=
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Fetch shipment data:

```bash
python scripts/fetch-shipping-stats.py
```

Generate metrics:

```bash
python scripts/generate-shipping-metrics.py
```

---

## Key Finding

The analysis identified that InPost shipments may be delayed by operational activities related to Poczta Polska handling.

The proposed improvement separates shipment dispatch activities for different carriers while preserving the existing customer-facing process.

---

## Disclaimer

This repository is intended for process analysis and educational purposes.

Customer data, order details, and other sensitive information are not included in the repository.

