"""Basic tests for marketplace parser package."""

import pytest
from marketplace_parser import __version__


def test_version():
    """Test that version is defined."""
    assert __version__ == "0.1.0"


def test_import():
    """Test that package can be imported."""
    import marketplace_parser

    assert marketplace_parser is not None
