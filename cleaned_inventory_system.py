#!/usr/bin/env python3
"""
cleaned_inventory_system.py
A minimal inventory example with defensive checks and logging.
"""

import logging
from typing import Dict

# Global inventory store (item -> quantity)
stock_data: Dict[str, int] = {}

def configure_logging() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s: %(message)s"
    )

def addItem(item, qty) -> None:
    """
    Add qty of item to stock_data.
    - item will be converted to str
    - qty will be converted to int if possible
    - raises ValueError for invalid qty
    """
    # convert item to string for consistent keys
    if not isinstance(item, str):
        item = str(item)

    # convert qty to int (if possible) and validate
    try:
        qty_int = int(qty)
    except (TypeError, ValueError):
        raise ValueError(f"Quantity must be an integer (got {qty!r})")

    if qty_int < 0:
        raise ValueError("Quantity to add must be non-negative")

    stock_data[item] = stock_data.get(item, 0) + qty_int
    logging.info("Added %d of %s. New qty: %d", qty_int, item, stock_data[item])

def removeItem(item, qty) -> None:
    """
    Remove qty of item from stock_data.
    Raises ValueError if insufficient stock or invalid qty.
    """
    # convert item and validate qty similar to addItem
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
    """Return stock quantity for item (item converted to str)."""
    if not isinstance(item, str):
        item = str(item)
    return stock_data.get(item, 0)

def main() -> None:
    configure_logging()
    logging.info("Starting inventory demo")

    # Good example
    try:
        addItem("apple", 10)
        addItem("banana", "5")   # string numeric - allowed
    except Exception as exc:
        logging.error("Error during add: %s", exc)

    # The problematic example from your traceback:
    try:
        # this will raise a ValueError now instead of causing TypeError
        addItem(123, "ten")  # invalid types, handled gracefully
    except Exception as exc:
        logging.error("Failed to add invalid item: %s", exc)

    # Show current stock
    logging.info("Current stock data: %s", stock_data)

if __name__ == "__main__":
    main()
