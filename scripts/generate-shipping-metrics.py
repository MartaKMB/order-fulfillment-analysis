import csv
from collections import Counter
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

INPUT_FILE = PROJECT_ROOT / "data" / "shipping-methods.csv"
OUTPUT_FILE = PROJECT_ROOT / "docs" / "metrics.md"

METHOD_MAPPING = {
    "Inpost Paczkomaty": "InPost",
    "Inpost kurier": "InPost",
    "Poczta Polska": "Poczta Polska",
    "Darmowa dostawa [Poczta Polska]": "Poczta Polska",
    "Pocztex": "Poczta Polska",
    "No shipping method": "Produkty online / brak wysyłki",
}


def normalize_method(method: str) -> str:
    return METHOD_MAPPING.get(method, f"Inne: {method}")


def main():
    counter = Counter()

    with INPUT_FILE.open(newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            raw_method = row["shipping_method"]
            normalized_method = normalize_method(raw_method)
            counter[normalized_method] += 1

    total = sum(counter.values())

    lines = [
        "# Shipping Metrics",
        "",
        "## Shipping Method Distribution",
        "",
        "Data source: WooCommerce REST API",
        "",
        "Field: `shipping_lines[].method_title`",
        "",
        "| Shipping group | Orders | Share |",
        "|---|---:|---:|",
    ]

    for method, count in counter.most_common():
        share = count / total * 100
        lines.append(f"| {method} | {count} | {share:.1f}% |")

    lines.extend([
        "",
        "## Observation",
        "",
        "The analyzed orders were grouped into business-level shipment categories.",
        "",
        "InPost includes both parcel locker and courier shipment methods.",
        "",
        "Poczta Polska includes standard Polish Post shipments, Pocztex, and free shipping orders fulfilled through Polish Post.",
        "",
        "Orders without a shipping method are treated as online products or records not requiring physical shipment.",
    ])

    lines.extend([
        "",
        "## Data Privacy Note",
        "",
        "The analysis is based on WooCommerce order data.",
        "",
        "Raw order-level data is not committed to the repository.",
        "Only aggregated metrics are included in the documentation.",
        "",
        "Customer personal information, addresses, email addresses, and order details are excluded from version control.",
    ])

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text("\n".join(lines), encoding="utf-8")

    print(f"Generated: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
