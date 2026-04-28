"""Unit tests for pure utility functions in module.base.utils."""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import pytest
from module.base.utils import (
    area_offset,
    area_pad,
    area_size,
    area_limit,
    limit_in,
    ensure_int,
    xywh2xyxy,
    xyxy2xywh,
    float2str,
    point_in_area,
    area_in_area,
    area_cross_area,
    random_normal_distribution_int,
)


class TestAreaOffset:
    def test_basic(self):
        assert area_offset((0, 0, 10, 10), (5, 5)) == (5, 5, 15, 15)

    def test_negative_offset(self):
        assert area_offset((10, 10, 20, 20), (-5, -5)) == (5, 5, 15, 15)

    def test_zero_offset(self):
        assert area_offset((1, 2, 3, 4), (0, 0)) == (1, 2, 3, 4)


class TestAreaPad:
    def test_basic(self):
        assert area_pad((0, 0, 100, 100), 10) == (10, 10, 90, 90)

    def test_zero_pad(self):
        assert area_pad((0, 0, 50, 50), 0) == (0, 0, 50, 50)

    def test_default_pad(self):
        result = area_pad((0, 0, 100, 100))
        assert result == (10, 10, 90, 90)


class TestAreaSize:
    def test_square(self):
        assert area_size((0, 0, 100, 100)) == (100, 100)

    def test_rectangle(self):
        assert area_size((10, 20, 110, 70)) == (100, 50)


class TestLimitIn:
    def test_within_range(self):
        assert limit_in(5, 0, 10) == 5

    def test_below_lower(self):
        assert limit_in(-5, 0, 10) == 0

    def test_above_upper(self):
        assert limit_in(15, 0, 10) == 10

    def test_at_boundary(self):
        assert limit_in(0, 0, 10) == 0
        assert limit_in(10, 0, 10) == 10


class TestEnsureInt:
    def test_single_float(self):
        result = ensure_int(1.7)
        assert result == 1

    def test_multiple_values(self):
        result = ensure_int(1.5, 2.7)
        assert result == [1, 2]


class TestCoordConversion:
    def test_xywh2xyxy(self):
        assert xywh2xyxy((10, 20, 30, 40)) == (10, 20, 40, 60)

    def test_xyxy2xywh(self):
        assert xyxy2xywh((10, 20, 40, 60)) == (10, 20, 30, 40)

    def test_roundtrip(self):
        original = (5, 10, 50, 80)
        assert xyxy2xywh(xywh2xyxy(original)) == original


class TestFloat2Str:
    def test_basic(self):
        result = float2str(3.14159, decimal=2)
        assert result == "3.14"

    def test_integer(self):
        result = float2str(5.0, decimal=0)
        assert result == "5.0"


class TestPointInArea:
    def test_inside(self):
        assert point_in_area((50, 50), (0, 0, 100, 100)) is True

    def test_outside(self):
        assert point_in_area((200, 200), (0, 0, 100, 100)) is False


class TestAreaCrossArea:
    def test_overlapping(self):
        assert area_cross_area((0, 0, 50, 50), (25, 25, 75, 75)) is True

    def test_non_overlapping(self):
        assert area_cross_area((0, 0, 10, 10), (50, 50, 100, 100)) is False


class TestRandomNormalDist:
    def test_within_range(self):
        for _ in range(20):
            val = random_normal_distribution_int(1, 10)
            assert 1 <= val <= 10

    def test_equal_bounds(self):
        val = random_normal_distribution_int(5, 5)
        assert val == 5
