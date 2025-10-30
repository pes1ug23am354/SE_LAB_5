import logging
from typing import Dict

stock_data: Dict[str, int] = {}

def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s: %(message)s"
    )

def addItem(item, qty) -> None:
    if not isinstance(item, str):
        item = str(item)
    try:
        qty_int = int(qty)
    except (TypeError, ValueError):
        raise ValueError(f"Quantity must be an integer (got {qty!r})")
    if qty_int < 0:
        raise ValueError("Quantity to add must be non-negative")
    stock_data[item] = stock_data.get(item, 0) + qty_int
    logging.info("Added %d of %s. New qty: %d", qty_int, item, stock_data[item])

def removeItem(item, qty) -> None:
    if not isinstance(item, str):
        item = str(item)
    try:
        qty_int = int(qty)
    except (TypeError, ValueError):
        raise ValueError(f"Quantity must be an integer (got {qty!r})")
    if qty_int <= 0:
        raise ValueError("Quantity to remove must be positive")
    current = stock_data.get(item, 0)
    if qty_int > current:
        raise ValueError(f"Not enough stock of {item} to remove ({qty_int} > {current})")
    stock_data[item] = current - qty_int
    logging.info("Removed %d of %s. New qty: %d", qty_int, item, stock_data[item])

def getStock(item) -> int:
    if not isinstance(item, str):
        item = str(item)
    return stock_data.get(item, 0)

def main() -> None:
    configure_logging()
    logging.info("Starting inventory demo")
    try:
        addItem("apple", 10)
        addItem("banana", "5")
    except Exception as exc:
        logging.error("Error during add: %s", exc)
    try:
        addItem(123, "ten")
    except Exception as exc:
        logging.error("Failed to add invalid item: %s", exc)
    logging.info("Current stock data: %s", stock_data)

if __name__ == "__main__":
    main()
