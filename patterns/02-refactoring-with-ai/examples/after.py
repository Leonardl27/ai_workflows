"""
after.py — The same sales processing logic, refactored.

Changes made and why:
- Extracted tax rates into a config dict (was: magic numbers scattered in if/elif)
- Separated validation, calculation, and formatting into pure functions
- Used context manager for file handling (was: manual open/close)
- Replaced print statements with structured return data
- Made each function independently testable

The public interface (process_sales) keeps the same signature and return shape.
"""

import csv
import logging
from dataclasses import dataclass
from datetime import datetime

logger = logging.getLogger(__name__)

# Tax rates by region — extracted from the if/elif chain.
# Single source of truth; easy to update or load from config.
TAX_RATES = {
    "EU": 1.20,
    "UK": 1.20,
    "CA": 1.13,
}

BULK_DISCOUNT_THRESHOLD = 100
BULK_DISCOUNT_RATE = 0.90


@dataclass
class SaleRecord:
    product_id: str
    quantity: int
    unit_price: float
    region: str
    date: str


def validate_row(row: dict) -> SaleRecord | None:
    """Validate a CSV row and return a SaleRecord, or None if invalid."""
    product_id = row.get("product_id")
    quantity_raw = row.get("quantity")
    price_raw = row.get("unit_price")

    if not product_id or not quantity_raw or not price_raw:
        return None

    quantity = int(quantity_raw)
    price = float(price_raw)

    if quantity <= 0 or price <= 0:
        return None

    return SaleRecord(
        product_id=product_id,
        quantity=quantity,
        unit_price=price,
        region=row.get("region", "US"),
        date=row.get("date", ""),
    )


def calculate_subtotal(record: SaleRecord) -> float:
    """Calculate subtotal with bulk discount and regional tax.

    Pure function — no side effects, easy to test with any inputs.
    """
    subtotal = record.quantity * record.unit_price

    if record.quantity > BULK_DISCOUNT_THRESHOLD:
        subtotal *= BULK_DISCOUNT_RATE

    tax_multiplier = TAX_RATES.get(record.region, 1.0)
    subtotal *= tax_multiplier

    return round(subtotal, 2)


def format_date(date_str: str) -> str:
    """Convert YYYY-MM-DD to MM/DD/YYYY, or return 'N/A' for empty/invalid input."""
    if not date_str:
        return "N/A"
    try:
        return datetime.strptime(date_str, "%Y-%m-%d").strftime("%m/%d/%Y")
    except ValueError:
        return "N/A"


def process_sales(filepath: str) -> dict:
    """Process sales CSV and return results, total, and errors.

    Same signature and return shape as the original — callers don't need to change.
    """
    results = []
    errors = []
    total = 0.0

    with open(filepath, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                record = validate_row(row)
                if record is None:
                    errors.append(f"Invalid row: {row}")
                    continue

                subtotal = calculate_subtotal(record)
                total += subtotal

                results.append({
                    "product_id": record.product_id,
                    "quantity": record.quantity,
                    "unit_price": record.unit_price,
                    "subtotal": subtotal,
                    "region": record.region,
                    "date": format_date(record.date),
                })
            except Exception as e:
                errors.append(f"Error processing row {row}: {e}")

    logger.info("Processed %d sales, total revenue: %.2f", len(results), total)
    if errors:
        logger.warning("%d errors encountered during processing", len(errors))

    return {"results": results, "total": round(total, 2), "errors": errors}
