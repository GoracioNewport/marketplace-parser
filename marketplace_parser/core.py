"""Core marketplace parser functionality."""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class Product:
    """Product information."""
    id: str
    name: str
    price: Optional[float]
    seller_id: str
    url: str


@dataclass
class Seller:
    """Seller information."""
    id: str
    name: str
    ogrn: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    url: str


class MarketplaceParser(ABC):
    """Base class for marketplace parsers."""
    
    def __init__(self, base_url: str):
        """Initialize parser with marketplace base URL."""
        self.base_url = base_url
    
    @abstractmethod
    def search_products(self, keyword: str, max_pages: int = 5) -> List[Product]:
        """Search for products by keyword."""
        pass
    
    @abstractmethod
    def get_seller_info(self, seller_id: str) -> Optional[Seller]:
        """Get seller information by seller ID."""
        pass
    
    def get_sellers_by_keyword(self, keyword: str, max_pages: int = 5) -> List[Seller]:
        """Get all sellers for products matching keyword."""
        products = self.search_products(keyword, max_pages)
        sellers = {}
        
        for product in products:
            if product.seller_id not in sellers:
                seller_info = self.get_seller_info(product.seller_id)
                if seller_info:
                    sellers[product.seller_id] = seller_info
        
        return list(sellers.values())
