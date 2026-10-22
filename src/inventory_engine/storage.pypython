import json
from pathlib import Path

from .models import Product, PerishableProduct
from .exceptions import StorageError


class InventoryStorage:
    """Save and load inventory data in JSON format."""

    @staticmethod
    def save(inventory, file_path):
        path = Path(file_path)

        data = []
        for product in inventory.list_products():
            item = {
                "product_id": product.product_id,
                "name": product.name,
                "price": str(product.price),
                "quantity": product.quantity,
                "product_type": (
                    "perishable"
                    if isinstance(product, PerishableProduct)
                    else "standard"
                ),
            }

            if isinstance(product, PerishableProduct):
                item["expiry_date"] = product.expiry_date

            data.append(item)

        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(
                json.dumps(data, indent=4),
                encoding="utf-8",
            )
        except (OSError, TypeError, ValueError) as exc:
            raise StorageError(f"Could not save inventory: {exc}") from exc

    @staticmethod
    def load(inventory, file_path):
        path = Path(file_path)

        try:
            data = json.loads(path.read_text(encoding="utf-8"))

            if not isinstance(data, list):
                raise ValueError("Inventory file must contain a JSON list.")

            products = []
            for item in data:
                if not isinstance(item, dict):
                    raise ValueError("Each product must be a JSON object.")

                if item.get("product_type") == "perishable":
                    product = PerishableProduct(
                        item["product_id"],
                        item["name"],
                        item["price"],
                        item["quantity"],
                        item["expiry_date"],
                    )
                else:
                    product = Product(
                        item["product_id"],
                        item["name"],
                        item["price"],
                        item["quantity"],
                    )

                products.append(product)

        except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
            raise StorageError(f"Could not load inventory: {exc}") from exc

        # Validate all products before replacing the existing inventory.
        product_ids = [product.product_id for product in products]
        if len(product_ids) != len(set(product_ids)):
            raise StorageError("Inventory file contains duplicate product IDs.")

        inventory._products = {
            product.product_id: product for product in products
        }
