import pytest

from src.inventory_engine.models import Product
from src.inventory_engine.exceptions import InvalidProductError


def test_product_creation():
    product = Product("P001", "Notebook", 50, 10)

    assert product.product_id == "P001"
    assert product.name == "Notebook"
    assert product.quantity == 10
    assert product.total_value == 500


def test_product_rejects_negative_price():
    with pytest.raises(InvalidProductError):
        Product("P001", "Notebook", -50, 10)


def test_product_rejects_negative_quantity():
    with pytest.raises(InvalidProductError):
        Product("P001", "Notebook", 50, -1)


def test_product_rejects_empty_name():
    with pytest.raises(InvalidProductError):
        Product("P001", "", 50, 10)
