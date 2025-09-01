"""Basic tests for marketplace parser package."""

import pytest
from marketplace_parser import __version__, MarketplaceParser, WildberriesParser
from marketplace_parser.core import Product, Seller


def test_version():
    """Test that version is defined."""
    assert __version__ == "0.1.0"


def test_import():
    """Test that package can be imported."""
    import marketplace_parser

    assert marketplace_parser is not None


def test_wildberries_parser_creation():
    """Test WildberriesParser can be created."""
    parser = WildberriesParser()
    assert isinstance(parser, MarketplaceParser)
    assert parser.base_url == "https://www.wildberries.ru"


def test_product_dataclass():
    """Test Product dataclass."""
    product = Product(
        id="123",
        name="Test Product",
        price=100.0,
        seller_id="seller123",
        url="https://example.com/product"
    )
    assert product.id == "123"
    assert product.name == "Test Product"
    assert product.price == 100.0


def test_seller_dataclass():
    """Test Seller dataclass."""
    seller = Seller(
        id="seller123",
        name="Test Seller",
        ogrn="1234567890123",
        email="test@example.com",
        phone="+7-123-456-7890",
        url="https://example.com/seller"
    )
    assert seller.id == "seller123"
    assert seller.ogrn == "1234567890123"
