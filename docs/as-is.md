# AS-IS: Order Fulfillment Process

## Purpose

This document describes the current order fulfillment process of a Polish e-commerce store and identifies potential process bottlenecks and improvement opportunities.

---

## Scope

### Included

* order placement
* payment processing
* payment verification
* order packaging
* shipment preparation
* shipment dispatch
* customer shipment notification

### Excluded

* returns
* complaints
* inventory management
* post-delivery customer support

---

## Process Diagram

![AS-IS BPMN](../diagrams/as-is-bpmn.png)

---

## Process Participants

The process responsibilities are described using business roles.

In the analyzed organization, all operational activities are currently performed by the store owner.

| Participant                   | Responsibility                                          |
| ----------------------------- | ------------------------------------------------------- |
| Customer                      | Places an order and selects payment and shipping method |
| Sales                         | Receives and handles the order                          |
| Finance                       | Verifies payment                                        |
| Warehouse                     | Packs and dispatches the order                          |
| Payment Provider (Przelewy24) | Confirms online payment                                 |

---

## Payment Flow

Customers can choose between two payment methods:

* Przelewy24
* Traditional bank transfer

### Przelewy24

The payment confirmation is received automatically from the external payment provider.

### Traditional Bank Transfer

The process waits for payment confirmation and requires manual verification.

If payment is not received within 7 days, the order is cancelled.

---

## Shipping Flow

Available shipping methods:

* InPost Paczkomaty
* InPost Kurier
* Poczta Polska

Orders are packed after successful payment verification.

The current process uses a shared shipment dispatch window aligned with the operational schedule of Poczta Polska.

Customers receive a shipment notification after the package has been dispatched.

---

## Process Assumptions

The analysis is based on the current operational model of a small e-commerce business.

The BPMN diagram focuses on business activities and process flow rather than organizational structure.

---

## Key Observations

### Observation 1

The order fulfillment process supports multiple payment methods and shipment providers.

### Observation 2

InPost and Poczta Polska shipments are handled within the same operational shipment flow.

### Observation 3

Traditional bank transfers require manual verification and may introduce processing delays.

---

## Identified Pain Point

The current process uses a shared shipment dispatch schedule for multiple shipment providers.

This may increase lead time for InPost orders, even though InPost shipments could potentially be dispatched independently from Poczta Polska shipments.

---

## Supporting Data

See:

* `docs/metrics.md`

for shipment method distribution based on WooCommerce order data.

---

## Open Questions

* Can InPost shipments be dispatched independently from Poczta Polska shipments?
* What operational impact would a separate InPost dispatch flow introduce?
* Can WooCommerce support separate shipment handling rules for each carrier?
* What is the average time between payment confirmation and shipment dispatch?
