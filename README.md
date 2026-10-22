# Inventory Management Engine

A Python-based inventory management system that supports product validation, stock management, inventory valuation, and JSON data persistence through a command-line interface (CLI).

## Features

- Add, view, update, and remove products.
- Validate product details and stock quantities.
- Support regular and perishable products.
- Calculate total inventory value.
- Save and load inventory data using JSON.
- Handle errors such as duplicate products, missing products, and insufficient stock.
- Provide CLI commands for common inventory operations.
- Include automated unit tests using pytest.

## Technologies Used

- Python 3.10+
- Object-Oriented Programming (OOP)
- JSON
- argparse
- pytest
- setuptools

## Project Structure

```text
inventory-management-engine/
├── src/
│   └── inventory_engine/
│       ├── __init__.py
│       ├── exceptions.py
│       ├── models.py
│       ├── inventory.py
│       ├── storage.py
│       └── cli.py
├── tests/
│   ├── test_models.py
│   ├── test_inventory.py
│   └── test_storage.py
├── example.py
├── inventory_data.json
├── pyproject.toml
├── README.md
└── .gitignore
```

## Installation

Clone the repository and navigate to the project folder.

```bash
git clone https://github.com/harshaadurada-ops/inventory-management-engine.git
cd inventory-management-engine
```

Create and activate a virtual environment.

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the project and development dependencies.

```powershell
python -m pip install -e ".[dev]"
```

## Usage

List products:

```powershell
inventory list
```

Display the inventory summary:

```powershell
inventory summary
```

Add a product:

```powershell
inventory add --id P003 --name Notebook --price 120 --quantity 10
```

Update stock:

```powershell
inventory update-stock --id P003 --quantity 5
```

Remove a product:

```powershell
inventory remove --id P003
```

Run the example script:

```powershell
python example.py
```

## Run Tests

```powershell
python -m pytest tests -v
```

## Learning Outcomes

This project demonstrates Python package development, object-oriented programming, input validation, custom exceptions, JSON persistence, command-line interfaces, and automated testing.

## Author

Harsha




Harsha

=======
# inventory-management-engine
A Python-based inventory management package with product validation, stock management, JSON persistence, a command-line interface, and automated tests.
>>>>>>> 46680999ac21a8732a856cd3682bbca7d49dcea9
