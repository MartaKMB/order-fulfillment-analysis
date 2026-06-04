# TO-BE: Order Fulfillment Process Improvement

## Goal

Align shipment handling with the actual characteristics of each shipment provider and reduce unnecessary waiting time in the fulfillment process.

---

## Background

Analysis of the current process identified a shared shipment workflow for multiple shipment providers.

WooCommerce shipment metrics indicate that:

* InPost shipment methods account for approximately 49% of analyzed orders.
* Poczta Polska shipment methods account for approximately 39% of analyzed orders.
* The remaining orders are digital products or orders without physical shipment requirements.

The current process causes InPost shipments to be influenced by operational activities required for Poczta Polska shipments.

---

## Proposed Change

Separate InPost and Poczta Polska dispatch activities.

### Current State

```text
InPost shipments
        ↓
Shared shipment workflow
        ↓
Poczta Polska-related activities
```

### Future State

```text
InPost shipments
        ↓
Independent dispatch flow

Poczta Polska shipments
        ↓
Dedicated dispatch flow
```

---

## Process Principles

### InPost

* Orders that are paid and packed can be dispatched at the next available shipment opportunity.
* Dispatch does not depend on Poczta Polska operational requirements.

### Poczta Polska

* Existing shipment procedures remain unchanged.
* Existing operational constraints remain unchanged.

---

## Expected Benefits

| Benefit                      | Description                                                             |
| ---------------------------- | ----------------------------------------------------------------------- |
| Faster InPost dispatch       | InPost shipments no longer wait for Poczta Polska-related activities    |
| Reduced lead time            | Customers receive shipment confirmation earlier                         |
| Better process alignment     | Shipment handling reflects the capabilities of each carrier             |
| Reduced operational friction | Routine Poczta Polska activities have less impact on InPost fulfillment |

---

## Risks

| Risk                                      | Impact                                                 | Mitigation                                      |
| ----------------------------------------- | ------------------------------------------------------ | ----------------------------------------------- |
| Additional operational effort             | More frequent shipment preparation and dispatch        | Monitor workload and adjust dispatch frequency  |
| Increased process complexity              | Additional shipment handling decisions                 | Define clear fulfillment rules                  |
| Limited benefit during low-volume periods | Faster dispatch may not significantly reduce lead time | Review fulfillment metrics after implementation |

---

## Success Metrics

The following metrics should be monitored after implementation:

| Metric                                        | Expected Trend |
| --------------------------------------------- | -------------- |
| Average payment-to-shipment time (InPost)     | Decrease       |
| Average order lead time                       | Decrease       |
| Number of delayed InPost shipments            | Decrease       |
| Customer inquiries related to shipment status | Decrease       |

---

## Future Considerations

The analysis identified several operational challenges related to Poczta Polska:

* manual shipment preparation,
* limited opening hours,
* queue waiting time,
* additional customer support related to shipment issues.

A separate business analysis may be conducted to evaluate whether maintaining Poczta Polska as a shipment option provides sufficient customer value relative to the operational effort required.

This topic is considered outside the scope of the current process improvement initiative.
