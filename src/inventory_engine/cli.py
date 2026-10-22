import argparse
import sys
from pathlib import Path

from .exceptions import InventoryError
from .models import Product, PerishableProduct
from .inventory import Inventory
from .storage import InventoryStorage


def main():
    parser = argparse.ArgumentParser(
        description="Inventory Management Engine"
    )
    parser.add_argument(
        "--file",
        default="inventory_data.json",
        help="Path to the inventory JSON file",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("list", help="List all products")

    add_parser = subparsers.add_parser("add", help="Add a product")
    add_parser.add_argument("--id", required=True, help="Product ID")
    add_parser.add_argument("--name", required=True, help="Product name")
    add_parser.add_argument("--price", required=True, type=float, help="Unit price")
    add_parser.add_argument("--quantity", required=True, type=int, help="Quantity")

    update_parser = subparsers.add_parser("update-stock", help="Change product quantity")
    update_parser.add_argument("--id", required=True, help="Product ID")
    update_parser.add_argument("--quantity", required=True, type=int, help="Quantity change")

    remove_parser = subparsers.add_parser("remove", help="Remove a product")
    remove_parser.add_argument("--id", required=True, help="Product ID")

    subparsers.add_parser("summary", help="Show inventory totals")

    args = parser.parse_args()
    file_path = Path(args.file)
    inventory = Inventory()
    storage = InventoryStorage()

    try:
        if file_path.exists():
            storage.load(inventory, file_path)

        if args.command == "list":
            products = inventory.list_products()
            if not products:
                print("Inventory is empty.")
            else:
                for product in products:
                    print(
                        f"{product.product_id} | {product.name} | "
                        f"Price: {product.price} | Quantity: {product.quantity}"
                    )

        elif args.command == "add":
            product = Product(
                product_id=args.id,
                name=args.name,
                price=args.price,
                quantity=args.quantity,
            )
            inventory.add_product(product)
            storage.save(inventory, file_path)
            print(f"Added product: {product.name}")

        elif args.command == "update-stock":
            inventory.update_stock(args.id, args.quantity)
            storage.save(inventory, file_path)
            print(f"Updated stock for product: {args.id}")

        elif args.command == "remove":
            inventory.remove_product(args.id)
            storage.save(inventory, file_path)
            print(f"Removed product: {args.id}")

        elif args.command == "summary":
            print("Inventory Summary")
            print("-----------------")
            print("Total products:", inventory.total_products)
            print("Total inventory value:", inventory.total_inventory_value)

    except (InventoryError, ValueError, OSError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
