import os

# Set base URL for pytest-html report at module level
os.environ['PLAYWRIGHT_BASE_URL'] = "https://playwright.dev"  # Playwright-specific base URL for HTML report

def pytest_html_report_title(report):
    """Custom hook to set HTML report title and metadata."""
    # Set custom title for the HTML report
    report.title = "Playwright Test Report" 