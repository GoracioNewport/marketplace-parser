"""Utility functions for marketplace parsing."""

import time
from typing import Optional
import requests
from bs4 import BeautifulSoup


class HTTPClient:
    """HTTP client with rate limiting and retry logic."""
    
    def __init__(self, delay: float = 1.0, max_retries: int = 3):
        """Initialize HTTP client."""
        self.delay = delay
        self.max_retries = max_retries
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
    
    def get(self, url: str, **kwargs) -> Optional[requests.Response]:
        """Make GET request with retry logic."""
        for attempt in range(self.max_retries):
            try:
                response = self.session.get(url, **kwargs)
                response.raise_for_status()
                time.sleep(self.delay)  # Rate limiting
                return response
            except requests.RequestException as e:
                if attempt == self.max_retries - 1:
                    print(f"Failed to fetch {url}: {e}")
                    return None
                time.sleep(self.delay * (attempt + 1))  # Exponential backoff
        return None
    
    def get_soup(self, url: str, **kwargs) -> Optional[BeautifulSoup]:
        """Get BeautifulSoup object from URL."""
        response = self.get(url, **kwargs)
        if response:
            return BeautifulSoup(response.content, 'lxml')
        return None


def extract_text(element) -> str:
    """Safely extract text from BeautifulSoup element."""
    if element is None:
        return ""
    return element.get_text(strip=True)


def extract_attribute(element, attribute: str) -> str:
    """Safely extract attribute from BeautifulSoup element."""
    if element is None:
        return ""
    return element.get(attribute, "")
