"""Utility functions for area and point manipulation."""
import random


def area_offset(area, offset):
    """Offset an area by a given (x, y) offset.

    Args:
        area: Tuple of (x1, y1, x2, y2)
        offset: Tuple of (x_offset, y_offset)

    Returns:
        Offset area tuple
    """
    x1, y1, x2, y2 = area
    ox, oy = offset
    return (x1 + ox, y1 + oy, x2 + ox, y2 + oy)


def area_pad(area, pad=10):
    """Pad an area by a given amount (shrinks the area inward).

    Args:
        area: Tuple of (x1, y1, x2, y2)
        pad: Padding amount (default 10)

    Returns:
        Padded area tuple
    """
    x1, y1, x2, y2 = area
    return (x1 + pad, y1 + pad, x2 - pad, y2 - pad)


def area_size(area):
    """Get the size of an area.

    Args:
        area: Tuple of (x1, y1, x2, y2)

    Returns:
        Tuple of (width, height)
    """
    x1, y1, x2, y2 = area
    return (x2 - x1, y2 - y1)


def area_limit(area, limit):
    """Limit area coordinates within a given limit.

    Args:
        area: Tuple of (x1, y1, x2, y2)
        limit: Tuple of (x1, y1, x2, y2) representing limits

    Returns:
        Limited area tuple
    """
    x1, y1, x2, y2 = area
    lx1, ly1, lx2, ly2 = limit
    return (
        limit_in(x1, lx1, lx2),
        limit_in(y1, ly1, ly2),
        limit_in(x2, lx1, lx2),
        limit_in(y2, ly1, ly2)
    )


def limit_in(value, lower, upper):
    """Limit a value to be within a range.

    Args:
        value: Value to limit
        lower: Lower bound
        upper: Upper bound

    Returns:
        Clamped value
    """
    return max(lower, min(upper, value))


def ensure_int(*args):
    """Ensure values are integers.

    Args:
        *args: Values to convert

    Returns:
        Single int or list of ints
    """
    if len(args) == 1:
        return int(args[0])
    return [int(x) for x in args]


def xywh2xyxy(area):
    """Convert (x, y, w, h) to (x1, y1, x2, y2).

    Args:
        area: Tuple of (x, y, w, h)

    Returns:
        Tuple of (x1, y1, x2, y2)
    """
    x, y, w, h = area
    return (x, y, x + w, y + h)


def xyxy2xywh(area):
    """Convert (x1, y1, x2, y2) to (x, y, w, h).

    Args:
        area: Tuple of (x1, y1, x2, y2)

    Returns:
        Tuple of (x, y, w, h)
    """
    x1, y1, x2, y2 = area
    return (x1, y1, x2 - x1, y2 - y1)


def float2str(value, decimal=2):
    """Convert float to string with fixed decimal places.

    Args:
        value: Float value
        decimal: Number of decimal places

    Returns:
        String representation
    """
    if decimal == 0:
        return f"{value:.1f}"
    return f"{value:.{decimal}f}"


def point_in_area(point, area):
    """Check if a point is within an area.

    Args:
        point: Tuple of (x, y)
        area: Tuple of (x1, y1, x2, y2)

    Returns:
        True if point is within area
    """
    px, py = point
    x1, y1, x2, y2 = area
    return x1 <= px <= x2 and y1 <= py <= y2


def area_in_area(area1, area2):
    """Check if area1 is within area2.

    Args:
        area1: Tuple of (x1, y1, x2, y2)
        area2: Tuple of (x1, y1, x2, y2)

    Returns:
        True if area1 is completely within area2
    """
    a1_x1, a1_y1, a1_x2, a1_y2 = area1
    a2_x1, a2_y1, a2_x2, a2_y2 = area2
    return a2_x1 <= a1_x1 and a1_x2 <= a2_x2 and a2_y1 <= a1_y1 and a1_y2 <= a2_y2


def area_cross_area(area1, area2):
    """Check if two areas overlap.

    Args:
        area1: Tuple of (x1, y1, x2, y2)
        area2: Tuple of (x1, y1, x2, y2)

    Returns:
        True if areas overlap
    """
    a1_x1, a1_y1, a1_x2, a1_y2 = area1
    a2_x1, a2_y1, a2_x2, a2_y2 = area2
    # Check for non-overlapping conditions
    if a1_x2 <= a2_x1 or a2_x2 <= a1_x1:
        return False
    if a1_y2 <= a2_y1 or a2_y2 <= a1_y1:
        return False
    return True


def random_normal_distribution_int(lower, upper, sigma=None):
    """Generate random integer with normal distribution.

    Args:
        lower: Lower bound
        upper: Upper bound
        sigma: Standard deviation (optional)

    Returns:
        Random integer within bounds
    """
    if lower == upper:
        return lower

    mean = (lower + upper) / 2
    if sigma is None:
        sigma = (upper - lower) / 6  # 99.7% within bounds with 3 sigma

    while True:
        value = int(round(random.gauss(mean, sigma)))
        if lower <= value <= upper:
            return value
