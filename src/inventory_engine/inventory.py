from .models import Product
from .exceptions import (
    DuplicateProductError,
    ProductNotFoundError,
    InsufficientStockError,
)


class Inventory:
    """Manages products in the inventory."""

    def __init__(self):
        self._products = {}

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Product must be a Product object.")

        if product.product_id in self._products:
            raise DuplicateProductError(
                f"Product ID '{product.product_id}' already exists."
            )

        self._products[product.product_id] = product
        return product

    def get_product(self, product_id):
        if product_id not in self._products:
            raise ProductNotFoundError(
                f"Product '{product_id}' was not found."
            )
        return self._products[product_id]

    def remove_product(self, product_id):
        if product_id not in self._products:
            raise ProductNotFoundError(
                f"Product '{product_id}' was not found."
            )
        return self._products.pop(product_id)

    def update_stock(self, product_id, quantity_change):
        product = self.get_product(product_id)

        if isinstance(quantity_change, bool) or not isinstance(
            quantity_change, int
        ):
            raise ValueError("Stock change must be an integer.")

        new_quantity = product.quantity + quantity_change

        if new_quantity < 0:
            raise InsufficientStockError(
                f"Not enough stock for '{product_id}'."
            )

        product.quantity = new_quantity
        return product.quantity

    def list_products(self):
        return list(self._products.values())

    @property
    def total_products(self):
        return len(self._products)

    @property
    def total_inventory_value(self):
        return sum(
            (product.total_value for product in self._products.values()),
            start=0,
        )
