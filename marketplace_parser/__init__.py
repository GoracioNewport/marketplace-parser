"""
Marketplace Parser Package

A Python package for parsing marketplace data to extract seller information.
Supports multiple marketplaces including Wildberries.
"""

__version__ = "0.1.0"
__author__ = "GoracioNewport"

from .core import MarketplaceParser
from .marketplaces import WildberriesParser

__all__ = ["MarketplaceParser", "WildberriesParser"]
