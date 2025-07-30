import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session", autouse=True)
def browser_context_args():
    """Browser context arguments for all tests following official Playwright documentation."""
    
    return {
        # Base URL to use in actions like page.goto('/')
        "base_url": "https://playwright.dev",
        
        # Viewport settings for all pages in the context
        "viewport": {
            "width": 1920,
            "height": 1080,
        },
        
        # Ignore HTTPS errors during navigation
        "ignore_https_errors": True,
        
        # Populates context with given storage state (for authentication)
        # "storage_state": "state.json",  # Uncomment when you have auth state
        
        # Additional HTTP headers to be sent with every request
        "extra_http_headers": {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
        },
    }


@pytest.fixture(scope="session")
def browser_type_launch_args():
    """Browser launch arguments for all tests following official Playwright documentation."""
    return {
        "headless": True,  # Set to True for headless mode
        "slow_mo": 0,      # No slow motion in headless mode
        # Additional launch options can be added here
        # "args": ["--disable-web-security"],
    }


@pytest.fixture(scope="session")
def browser_name():
    """Default browser for all tests."""
    return "chromium"  # Options: chromium, firefox, webkit 