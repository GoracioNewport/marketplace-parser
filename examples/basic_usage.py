"""Basic usage example for marketplace parser."""

from marketplace_parser import WildberriesParser


def main():
    """Example usage of Wildberries parser."""
    # Create parser instance
    parser = WildberriesParser()
    
    # Search for products
    keyword = "ноутбук"
    print(f"Searching for products with keyword: {keyword}")
    
    # Get sellers for products matching keyword
    sellers = parser.get_sellers_by_keyword(keyword, max_pages=2)
    
    print(f"Found {len(sellers)} unique sellers:")
    for seller in sellers:
        print(f"- {seller.name} (ID: {seller.id})")
        if seller.ogrn:
            print(f"  OGRN: {seller.ogrn}")
        if seller.email:
            print(f"  Email: {seller.email}")
        if seller.phone:
            print(f"  Phone: {seller.phone}")
        print()


if __name__ == "__main__":
    main()
