# Marketplace Parser

A Python package for parsing marketplace data to extract seller information. Supports multiple marketplaces including Wildberries.

## Features

- **Multi-marketplace support** - Modular architecture for easy addition of new marketplaces
- **Seller information extraction** - Get seller details including OGRN, email, and phone
- **Rate limiting** - Built-in protection against being blocked
- **Retry logic** - Automatic retry on failed requests
- **Type safety** - Full type hints and mypy support

## Installation

This project uses Poetry for dependency management.

```bash
# Install dependencies
poetry install

# Activate virtual environment
poetry shell
```

## Usage

```python
from marketplace_parser import WildberriesParser

# Create parser instance
parser = WildberriesParser()

# Search for sellers by keyword
sellers = parser.get_sellers_by_keyword("ноутбук", max_pages=5)

# Print seller information
for seller in sellers:
    print(f"Seller: {seller.name}")
    print(f"OGRN: {seller.ogrn}")
    print(f"Email: {seller.email}")
    print(f"Phone: {seller.phone}")
```

## Development

```bash
# Add a new dependency
poetry add package-name

# Add a development dependency
poetry add --group dev package-name

# Run tests
poetry run pytest

# Format code
poetry run black .

# Check types
poetry run mypy .

# Sort imports
poetry run isort .
```

## Project Structure

```
marketplace-parser/
├── marketplace_parser/          # Main package
│   ├── core.py                 # Base classes and data models
│   ├── utils.py                # HTTP utilities and helpers
│   └── marketplaces/           # Marketplace-specific parsers
│       └── wildberries.py      # Wildberries parser
├── tests/                      # Test files
├── examples/                   # Usage examples
├── pyproject.toml             # Poetry configuration
└── README.md                  # This file
```

## Supported Marketplaces

- **Wildberries** - Russian marketplace (in development)

## Roadmap

- [ ] Implement Wildberries product search
- [ ] Implement seller page parsing
- [ ] Add OGRN lookup service integration
- [ ] Add more marketplaces (Ozon, AliExpress, etc.)
- [ ] Add data export functionality
- [ ] Add web interface
