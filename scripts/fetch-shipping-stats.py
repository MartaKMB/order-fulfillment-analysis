import os
from dotenv import load_dotenv
import csv
import requests
from collections import Counter
from pathlib import Path

load_dotenv()

STORE_URL = os.environ["WC_STORE_URL"].rstrip("/")
CONSUMER_KEY = os.environ["WC_CONSUMER_KEY"]
CONSUMER_SECRET = os.environ["WC_CONSUMER_SECRET"]

params = {
    "consumer_key": CONSUMER_KEY,
    "consumer_secret": CONSUMER_SECRET,
    "per_page": 100,
    "page": 1,
    "status": "completed",
}

shipping_counter = Counter()
rows = []

while True:
    response = requests.get(
        f"{STORE_URL}/wp-json/wc/v3/orders",
        params=params,
        timeout=30,
    )
    response.raise_for_status()

    orders = response.json()
    if not orders:
        break

    for order in orders:
        order_id = order["id"]
        order_date = order.get("date_created", "")
        shipping_lines = order.get("shipping_lines", [])

        if shipping_lines:
            method = shipping_lines[0].get("method_title", "Unknown")
        else:
            method = "No shipping method"

        shipping_counter[method] += 1

        rows.append({
            "order_id": order_id,
            "date_created": order_date,
            "shipping_method": method,
            "status": order.get("status", ""),
        })

    params["page"] += 1

output_dir = Path("data")
output_dir.mkdir(exist_ok=True)

output_file = output_dir / "shipping-methods.csv"

with output_file.open("w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(
        file,
        fieldnames=["order_id", "date_created", "shipping_method", "status"],
    )
    writer.writeheader()
    writer.writerows(rows)

print("Shipping method distribution:")
for method, count in shipping_counter.most_common():
    print(f"{method}: {count}")
