# TO-BE: Order Fulfillment Process Improvement

## Goal

Reduce shipment lead time for InPost orders by separating InPost dispatch operations from the Poczta Polska shipment schedule.

---

## Background

Analysis of the current fulfillment process identified a shared shipment dispatch flow for multiple shipment providers.

WooCommerce shipment metrics indicate that:

* InPost shipment methods account for approximately 49% of analyzed orders.
* Poczta Polska shipment methods account for approximately 39% of analyzed orders.
* The remaining orders are digital products or orders without physical shipment requirements.

Despite the significant share of InPost shipments, the current operational process follows a shipment schedule influenced by Poczta Polska handling requirements.

---

## Proposed Process Change

### Current State

```text
InPost shipments
        ↓
Shared shipment workflow
        ↓
Poczta Polska shipment window
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

* Orders paid and packed are dispatched at the next available shipment opportunity.
* Dispatch is independent from Poczta Polska operational constraints.

### Poczta Polska

* Existing shipment schedule remains unchanged.
* Existing operational procedures remain unchanged.

---

## Expected Benefits

| Benefit                           | Description                                                                           |
| --------------------------------- | --------------------------------------------------------------------------------------|
| Reduced lead time                 | InPost orders no longer wait for Poczta Polska dispatch activities                    |
| Faster customer communication     | Shipment notifications can be sent earlier                                            |
| Better process alignment          | Shipment handling reflects the actual capabilities of each carrier.                   |
| Simpler prioritization            | High-volume InPost orders can be processed independently from Poczta Polska shipments |

---

## Implementation Impact

### Operational Impact

Low.

The proposed solution changes shipment scheduling without changing payment handling, order verification, packaging, or customer communication processes.

### Technical Impact

Low.

No WooCommerce checkout changes are required.

The change primarily affects operational fulfillment procedures.

### Customer Impact

Positive.

Customers selecting InPost should receive shipment confirmation earlier.

---

## Risks

| Risk                                      | Impact                                                 | Mitigation                           |
|-------------------------------------------|--------------------------------------------------------|--------------------------------------|
| Additional operational effort             | More frequent shipment preparation and dispatch        | Monitor workload and adjust dispatch frequency |
| Increased process complexity              | Additional shipment handling decisions                 | Define clear shipment handling rules |
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

* manual address handling,
* limited opening hours,
* queue waiting time,
* occasional shipment loss requiring additional customer support effort.

These observations may justify a separate business analysis evaluating the long-term value of maintaining Poczta Polska as a shipment provider.

This topic is considered outside the scope of the current process improvement initiative.
