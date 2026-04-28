"""Unit tests for config deep-access utilities in module.config.deep."""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

import pytest
from module.config.deep import (
    deep_get,
    deep_set,
    deep_exist,
    deep_default,
    deep_pop,
)


SAMPLE = {
    "Scheduler": {
        "NextRun": {"value": "2024-01-01 00:00:00"},
        "Enable": True,
    },
    "Campaign": {"Name": "Campaign1"},
}


class TestDeepGet:
    def test_dot_notation(self):
        assert deep_get(SAMPLE, "Scheduler.Enable") is True

    def test_list_notation(self):
        assert deep_get(SAMPLE, ["Scheduler", "NextRun", "value"]) == "2024-01-01 00:00:00"

    def test_missing_key_returns_default(self):
        assert deep_get(SAMPLE, "Missing.Key") is None
        assert deep_get(SAMPLE, "Missing.Key", default="fallback") == "fallback"

    def test_shallow_key(self):
        result = deep_get(SAMPLE, "Campaign")
        assert result == {"Name": "Campaign1"}


class TestDeepExist:
    def test_existing_key(self):
        assert deep_exist(SAMPLE, "Scheduler.Enable") is True

    def test_missing_key(self):
        assert deep_exist(SAMPLE, "Scheduler.Nonexistent") is False


class TestDeepSet:
    def test_set_existing(self):
        d = {"a": {"b": 1}}
        deep_set(d, "a.b", 99)
        assert d["a"]["b"] == 99

    def test_set_new_key(self):
        d = {"a": {}}
        deep_set(d, "a.new_key", "value")
        assert d["a"]["new_key"] == "value"


class TestDeepDefault:
    def test_key_not_present(self):
        d = {"a": {}}
        deep_default(d, "a.missing", "default_val")
        assert d["a"]["missing"] == "default_val"

    def test_existing_key_not_overwritten(self):
        d = {"a": {"b": "original"}}
        deep_default(d, "a.b", "new_val")
        assert d["a"]["b"] == "original"


class TestDeepPop:
    def test_pop_existing(self):
        d = {"a": {"b": 42}}
        val = deep_pop(d, "a.b")
        assert val == 42
        assert "b" not in d["a"]

    def test_pop_missing(self):
        d = {"a": {}}
        val = deep_pop(d, "a.missing", default="fallback")
        assert val == "fallback"
