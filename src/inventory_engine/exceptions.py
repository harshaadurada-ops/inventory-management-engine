class InventoryError(Exception):
    """Base exception for inventory-related errors."""


class InvalidProductError(InventoryError):
    """Raised when product information is invalid."""


class DuplicateProductError(InventoryError):
    """Raised when a product ID already exists."""


class ProductNotFoundError(InventoryError):
    """Raised when a requested product does not exist."""


class InsufficientStockError(InventoryError):
    """Raised when requested stock exceeds available stock."""


class StorageError(InventoryError):
    """Raised when saving or loading inventory data fails."""
