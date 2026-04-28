"""Deep access utilities for nested dictionaries."""


def deep_get(d, keys, default=None):
    """Get value from nested dictionary using dot notation or list of keys.

    Args:
        d: Dictionary to search
        keys: String with dot notation or list of keys
        default: Default value if key not found

    Returns:
        Value at the key path or default
    """
    raise NotImplementedError


def deep_set(d, keys, value):
    """Set value in nested dictionary using dot notation or list of keys.

    Args:
        d: Dictionary to modify
        keys: String with dot notation or list of keys
        value: Value to set
    """
    raise NotImplementedError


def deep_exist(d, keys):
    """Check if a key path exists in nested dictionary.

    Args:
        d: Dictionary to search
        keys: String with dot notation or list of keys

    Returns:
        True if key path exists
    """
    raise NotImplementedError


def deep_default(d, keys, default):
    """Set default value if key path doesn't exist.

    Args:
        d: Dictionary to modify
        keys: String with dot notation or list of keys
        default: Default value to set if not exists
    """
    raise NotImplementedError


def deep_pop(d, keys, default=None):
    """Pop value from nested dictionary using dot notation or list of keys.

    Args:
        d: Dictionary to modify
        keys: String with dot notation or list of keys
        default: Default value if key not found

    Returns:
        Popped value or default
    """
    raise NotImplementedError
