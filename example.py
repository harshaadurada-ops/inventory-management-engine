from inventory_engine import Product, Inventory, InventoryStorage
from pathlib import Path

inventory = Inventory()

product = Product(
    product_id="P001",
    name="Keyboard",
    price=799.00,
    quantity=10
)

inventory.add_product(product)

print("INVENTORY MANAGEMENT ENGINE")
print("-" * 30)
print("Product:", product.name)
print("Quantity:", product.quantity)
print("Total inventory value:", inventory.total_inventory_value)

storage = InventoryStorage()
storage.save(inventory, Path("inventory_data.json"))

print("\nInventory saved to inventory_data.json")
