"""
before.py — A realistic example of code that needs refactoring.

This function processes sales data from a CSV export. It works, but it
mixes parsing, validation, business logic, and output formatting into
one monolithic function. It's hard to test, hard to modify, and the
magic numbers make it fragile.
"""

import csv
from datetime import datetime


def process_sales(filepath):
    results = []
    errors = []
    total = 0
    f = open(filepath, "r")
    reader = csv.DictReader(f)
    for row in reader:
        try:
            # validate
            if not row.get("product_id") or not row.get("quantity") or not row.get("unit_price"):
                errors.append(f"Row missing fields: {row}")
                continue
            qty = int(row["quantity"])
            price = float(row["unit_price"])
            if qty <= 0 or price <= 0:
                errors.append(f"Invalid values in row: {row}")
                continue

            # calculate
            subtotal = qty * price
            if qty > 100:
                subtotal = subtotal * 0.9  # bulk discount
            if row.get("region") == "EU":
                subtotal = subtotal * 1.2  # VAT
            elif row.get("region") == "UK":
                subtotal = subtotal * 1.2  # UK VAT
            elif row.get("region") == "CA":
                subtotal = subtotal * 1.13  # Canadian HST
            total += subtotal

            # format output
            results.append({
                "product_id": row["product_id"],
                "quantity": qty,
                "unit_price": price,
                "subtotal": round(subtotal, 2),
                "region": row.get("region", "US"),
                "date": datetime.strptime(row.get("date", ""), "%Y-%m-%d").strftime("%m/%d/%Y") if row.get("date") else "N/A",
            })
        except Exception as e:
            errors.append(f"Error processing row {row}: {e}")

    f.close()

    # print summary
    print(f"Processed {len(results)} sales")
    print(f"Total revenue: ${round(total, 2)}")
    if errors:
        print(f"Errors ({len(errors)}):")
        for e in errors:
            print(f"  - {e}")

    return {"results": results, "total": round(total, 2), "errors": errors}
