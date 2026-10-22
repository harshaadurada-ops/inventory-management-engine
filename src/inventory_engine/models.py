from decimal import Decimal, InvalidOperation
from .exceptions import InvalidProductError


class Product:
    """Represents a product in inventory."""

    def __init__(self, product_id, name, price, quantity):
        self._product_id = self._validate_text(product_id, "Product ID")
        self._name = self._validate_text(name, "Product name")
        self.price = price
        self.quantity = quantity

    @staticmethod
    def _validate_text(value, field_name):
        if not isinstance(value, str) or not value.strip():
            raise InvalidProductError(f"{field_name} cannot be empty.")
        return value.strip()

    @property
    def product_id(self):
        return self._product_id

    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        try:
            amount = Decimal(str(value))
        except (InvalidOperation, ValueError):
            raise InvalidProductError("Price must be a number.") from None
        if not amount.is_finite() or amount < 0:
            raise InvalidProductError("Price must be non-negative.")
        self._price = amount

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise InvalidProductError(
                "Quantity must be a non-negative integer."
            )
        self._quantity = value

    @property
    def total_value(self):
        return self.price * self.quantity

    def describe(self):
        return (
            f"{self.name} | ID: {self.product_id} | "
            f"Price: {self.price:.2f} | Stock: {self.quantity}"
        )


class PerishableProduct(Product):
    """Product that has an expiry date."""

    def __init__(self, product_id, name, price, quantity, expiry_date):
        super().__init__(product_id, name, price, quantity)
        self._expiry_date = self._validate_text(
            expiry_date, "Expiry date"
        )

    @property
    def expiry_date(self):
        return self._expiry_date

    def describe(self):
        return f"{super().describe()} | Expiry: {self.expiry_date}"
