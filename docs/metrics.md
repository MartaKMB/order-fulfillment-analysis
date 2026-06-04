# Shipping Metrics

## Shipping Method Distribution

Data source: WooCommerce REST API

Field: `shipping_lines[].method_title`

| Shipping group | Orders | Share |
|---|---:|---:|
| InPost | 304 | 48.7% |
| Poczta Polska | 242 | 38.8% |
| Produkty online / brak wysyłki | 78 | 12.5% |

## Observation

The analyzed orders were grouped into business-level shipment categories.

InPost includes both parcel locker and courier shipment methods.

Poczta Polska includes standard Polish Post shipments, Pocztex, and free shipping orders fulfilled through Polish Post.

Orders without a shipping method are treated as online products or records not requiring physical shipment.

## Data Privacy Note

The analysis is based on WooCommerce order data.

Raw order-level data is not committed to the repository.
Only aggregated metrics are included in the documentation.

Customer personal information, addresses, email addresses, and order details are excluded from version control.