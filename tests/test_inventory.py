import pytest

from src.inventory_engine.models import Product
from src.inventory_engine.inventory import Inventory
from src.inventory_engine.exceptions import (
    DuplicateProductError,
    ProductNotFoundError,
    InsufficientStockError,
)


def create_inventory():
    inventory = Inventory()
    inventory.add_product(Product("P001", "Notebook", 50, 10))
    return inventory


def test_add_product():
    inventory = create_inventory()

    assert inventory.total_products == 1
    assert inventory.get_product("P001").name == "Notebook"


def test_duplicate_product_is_rejected():
    inventory = create_inventory()

    with pytest.raises(DuplicateProductError):
        inventory.add_product(Product("P001", "Pen", 10, 5))


def test_missing_product_is_rejected():
    inventory = create_inventory()

    with pytest.raises(ProductNotFoundError):
        inventory.get_product("P999")


def test_update_stock():
    inventory = create_inventory()

    quantity = inventory.update_stock("P001", 5)

    assert quantity == 15


def test_insufficient_stock_is_rejected():
    inventory = create_inventory()

    with pytest.raises(InsufficientStockError):
        inventory.update_stock("P001", -20)


def test_remove_product():
    inventory = create_inventory()

    inventory.remove_product("P001")

    assert inventory.total_products == 0
