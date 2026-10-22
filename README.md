\# Inventory Management Engine



A Python-based inventory management package with product validation, stock management, JSON persistence, a command-line interface (CLI), and automated tests.



\## Features



\- Product creation and validation

\- Standard and perishable product support

\- Add, list, update, and remove products

\- Stock validation and custom exceptions

\- Inventory value calculations

\- JSON file persistence

\- Installable Python package with CLI commands

\- Automated tests using pytest



\## Technologies



\- Python

\- Object-Oriented Programming

\- JSON

\- pytest

\- setuptools

\- Git and GitHub



\## Installation



Clone the repository:



```bash

git clone YOUR\_REPOSITORY\_URL

cd inventory-management-engine

```



Create a virtual environment and install the package:



```powershell

python -m venv .venv

.\\.venv\\Scripts\\Activate.ps1

python -m pip install -e ".\[dev]"

```



\## Usage



List products:



```powershell

inventory list

```



Add a product:



```powershell

inventory add --id P003 --name Monitor --price 6500 --quantity 2

```



Update stock:



```powershell

inventory update-stock --id P002 --quantity 3

```



Remove a product:



```powershell

inventory remove --id P002

```



Display inventory totals:



```powershell

inventory summary

```



The CLI stores inventory data in `inventory\_data.json` by default.



\## Run Tests



```powershell

python -m pytest .\\tests -v

```



\## Project Structure



```text

src/inventory\_engine/

├── \_\_init\_\_.py

├── exceptions.py

├── models.py

├── inventory.py

├── storage.py

└── cli.py



tests/

pyproject.toml

README.md

.gitignore

```



\## Learning Outcomes



This project demonstrates Python packaging, object-oriented programming, exception handling, data validation, JSON persistence, CLI development, and automated testing.



\## Author



Harsha

