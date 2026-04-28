"""Deep access utilities for nested dictionaries."""


def _to_keys(keys):
    """Convert keys to list format.

    Args:
        keys: String with dot notation or list of keys

    Returns:
        List of keys
    """
    if isinstance(keys, str):
        return keys.split('.')
    return list(keys)


def deep_get(d, keys, default=None):
    """Get value from nested dictionary using dot notation or list of keys.

    Args:
        d: Dictionary to search
        keys: String with dot notation or list of keys
        default: Default value if key not found

    Returns:
        Value at the key path or default
    """
    keys = _to_keys(keys)
    current = d
    for key in keys:
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
    return current


def deep_set(d, keys, value):
    """Set value in nested dictionary using dot notation or list of keys.

    Args:
        d: Dictionary to modify
        keys: String with dot notation or list of keys
        value: Value to set
    """
    keys = _to_keys(keys)
    current = d
    for key in keys[:-1]:
        if key not in current:
            current[key] = {}
        current = current[key]
    current[keys[-1]] = value


def deep_exist(d, keys):
    """Check if a key path exists in nested dictionary.

    Args:
        d: Dictionary to search
        keys: String with dot notation or list of keys

    Returns:
        True if key path exists
    """
    keys = _to_keys(keys)
    current = d
    for key in keys:
        if not isinstance(current, dict) or key not in current:
            return False
        current = current[key]
    return True


def deep_default(d, keys, default):
    """Set default value if key path doesn't exist.

    Args:
        d: Dictionary to modify
        keys: String with dot notation or list of keys
        default: Default value to set if not exists
    """
    if not deep_exist(d, keys):
        deep_set(d, keys, default)


def deep_pop(d, keys, default=None):
    """Pop value from nested dictionary using dot notation or list of keys.

    Args:
        d: Dictionary to modify
        keys: String with dot notation or list of keys
        default: Default value if key not found

    Returns:
        Popped value or default
    """
    keys = _to_keys(keys)
    current = d
    for key in keys[:-1]:
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]

    if not isinstance(current, dict) or keys[-1] not in current:
        return default
    return current.pop(keys[-1])
