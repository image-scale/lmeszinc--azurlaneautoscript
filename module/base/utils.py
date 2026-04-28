"""Utility functions for area and point manipulation."""


def area_offset(area, offset):
    """Offset an area by a given (x, y) offset.

    Args:
        area: Tuple of (x1, y1, x2, y2)
        offset: Tuple of (x_offset, y_offset)

    Returns:
        Offset area tuple
    """
    raise NotImplementedError


def area_pad(area, pad=10):
    """Pad an area by a given amount.

    Args:
        area: Tuple of (x1, y1, x2, y2)
        pad: Padding amount (default 10)

    Returns:
        Padded area tuple
    """
    raise NotImplementedError


def area_size(area):
    """Get the size of an area.

    Args:
        area: Tuple of (x1, y1, x2, y2)

    Returns:
        Tuple of (width, height)
    """
    raise NotImplementedError


def area_limit(area, limit):
    """Limit area coordinates within a given limit."""
    raise NotImplementedError


def limit_in(value, lower, upper):
    """Limit a value to be within a range.

    Args:
        value: Value to limit
        lower: Lower bound
        upper: Upper bound

    Returns:
        Clamped value
    """
    raise NotImplementedError


def ensure_int(*args):
    """Ensure values are integers.

    Args:
        *args: Values to convert

    Returns:
        Single int or list of ints
    """
    raise NotImplementedError


def xywh2xyxy(area):
    """Convert (x, y, w, h) to (x1, y1, x2, y2).

    Args:
        area: Tuple of (x, y, w, h)

    Returns:
        Tuple of (x1, y1, x2, y2)
    """
    raise NotImplementedError


def xyxy2xywh(area):
    """Convert (x1, y1, x2, y2) to (x, y, w, h).

    Args:
        area: Tuple of (x1, y1, x2, y2)

    Returns:
        Tuple of (x, y, w, h)
    """
    raise NotImplementedError


def float2str(value, decimal=2):
    """Convert float to string with fixed decimal places.

    Args:
        value: Float value
        decimal: Number of decimal places

    Returns:
        String representation
    """
    raise NotImplementedError


def point_in_area(point, area):
    """Check if a point is within an area.

    Args:
        point: Tuple of (x, y)
        area: Tuple of (x1, y1, x2, y2)

    Returns:
        True if point is within area
    """
    raise NotImplementedError


def area_in_area(area1, area2):
    """Check if area1 is within area2."""
    raise NotImplementedError


def area_cross_area(area1, area2):
    """Check if two areas overlap.

    Args:
        area1: Tuple of (x1, y1, x2, y2)
        area2: Tuple of (x1, y1, x2, y2)

    Returns:
        True if areas overlap
    """
    raise NotImplementedError


def random_normal_distribution_int(lower, upper, sigma=None):
    """Generate random integer with normal distribution.

    Args:
        lower: Lower bound
        upper: Upper bound
        sigma: Standard deviation (optional)

    Returns:
        Random integer within bounds
    """
    raise NotImplementedError
