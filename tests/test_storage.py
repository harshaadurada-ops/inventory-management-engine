import json

from src.inventory_engine.models import Product, PerishableProduct
from src.inventory_engine.inventory import Inventory
from src.inventory_engine.storage import InventoryStorage


def test_save_and_load_inventory(tmp_path):
    inventory = Inventory()
    inventory.add_product(Product("P001", "Notebook", 50, 10))
    inventory.add_product(
        PerishableProduct("P002", "Milk", 30, 5, "2026-10-30")
    )

    file_path = tmp_path / "inventory.json"

    InventoryStorage.save(inventory, file_path)

    loaded_inventory = Inventory()
    InventoryStorage.load(loaded_inventory, file_path)

    assert loaded_inventory.total_products == 2
    assert loaded_inventory.get_product("P001").name == "Notebook"
    assert loaded_inventory.get_product("P001").quantity == 10
    assert loaded_inventory.total_inventory_value == 650
    assert loaded_inventory.get_product("P002").expiry_date == "2026-10-30"


def test_saved_file_contains_valid_json(tmp_path):
    inventory = Inventory()
    inventory.add_product(Product("P001", "Notebook", 50, 10))

    file_path = tmp_path / "inventory.json"
    InventoryStorage.save(inventory, file_path)

    data = json.loads(file_path.read_text(encoding="utf-8"))

    assert isinstance(data, list)
    assert data[0]["product_id"] == "P001"
    assert data[0]["quantity"] == 10
