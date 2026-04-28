"""Smoke tests: verify that key project modules are importable."""
import pytest


def test_import_base_utils():
    import module.base.utils


def test_import_base_filter():
    import module.base.filter


def test_import_base_timer():
    import module.base.timer


def test_import_base_decorator():
    import module.base.decorator


def test_import_config_deep():
    import module.config.deep


def test_import_config_utils():
    import module.config.utils


def test_import_config_generated():
    import module.config.config_generated


def test_import_config_manual():
    import module.config.config_manual


def test_import_config_env():
    import module.config.env


def test_import_config_server():
    import module.config.server


def test_import_exception():
    import module.exception


def test_import_logger():
    import module.logger


def test_import_map_map_grids():
    import module.map.map_grids


def test_import_ocr():
    import module.ocr.ocr


def test_import_statistics():
    import module.statistics.get_items
