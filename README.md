# Playwright Example Project

This project demonstrates Playwright automation testing with Python and Pytest, following the official Playwright documentation patterns and Testing Rules.

## Project Rules

This project follows the rules defined in `rules/Starting Rules.md` and `rules/Testing Rules.md`:

### Core Rules
- **Rule 1**: Use Playwright for browser automation
- **Rule 2**: Use Pytest for test framework
- **Rule 3**: Use Python as the programming language
- **Rule 4**: Only follow the official Playwright documents
- **Rule 5**: Only use Official Playwright Documentation for design patterns
- **Rule 6**: Use Playwright MCP to run the browser in order to find locators
- **Rule 7**: If you can't use Playwright MCP, open the browser and Find the locators
- **Rule 8**: Do not deviate, If you have Fix it
- **Rule 9**: Before writing any code, Make sure it meets these rules

### Commenting Rules
- **Rule 1**: Make sure to write short, concise comments for all code

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

## Installation

1. **Install Python dependencies:**
   ```bash
   python -m pip install -r requirements.txt
   ```

2. **Install Playwright browsers:**
   ```bash
   playwright install
   ```

## Configuration

This project follows the official Playwright documentation for test configuration:

### Base URL Configuration
The project uses base URL configuration as recommended in the [official Playwright documentation](https://playwright.dev/docs/test-use-options):

```python
# In conftest.py
@pytest.fixture(scope="session")
def browser_context_args():
    return {
        "base_url": "https://playwright.dev",
        # ... other options
    }
```

This allows tests to use relative URLs:
```python
# Instead of: page.goto("https://playwright.dev/")
page.goto("/")  # Uses base URL automatically
```

### Storage State Configuration
The project supports storage state for authentication as documented in the [official Playwright documentation](https://playwright.dev/docs/test-use-options):

```python
# In conftest.py
"storage_state": "state.json",  # For authentication
```

### Additional Configuration Options
Following the official documentation, the project includes:

- **Viewport settings**: `{"width": 1920, "height": 1080}`
- **HTTP headers**: Custom headers for all requests
- **HTTPS error handling**: `ignore_https_errors: True`
- **Browser launch options**: Headless mode, slow motion for debugging

## Running Tests

### Basic Test Execution
```bash
# Run all tests
pytest

# Run with verbose output
pytest -v
```

### Test Filtering by Markers
```bash
# Run only smoke tests (quick validation)
pytest -m smoke

# Run only regression tests (comprehensive)
pytest -m regression

# Run only slow tests
pytest -m slow

# Run all tests EXCEPT slow ones
pytest -m "not slow"
```

### Browser Selection
```bash
# Run with specific browser
pytest --browser chromium
pytest --browser firefox
pytest --browser webkit
```

### Headless/Headed Mode
```bash
# Run in headless mode (no browser UI)
pytest --headed=false

# Run with browser UI visible
pytest --headed=true
```

### Specific Test Files
```bash
# Run specific test file
pytest tests/test_example.py

# Run specific test class
pytest tests/test_example.py::TestExample

# Run specific test method
pytest tests/test_example.py::TestExample::test_basic_navigation
```

### HTML Reporter

This project includes HTML reporting functionality. After running tests, an HTML report is automatically generated in the `playwright-report/` directory.

**View the HTML report:**
- The report is generated at: `playwright-report/report.html`
- Open this file in your browser to view detailed test results
- The report includes test results, timing, and any failures with screenshots

**Features of the HTML report:**
- ✅ **Self-contained**: No external dependencies required
- ✅ **Detailed results**: Shows pass/fail status, timing, and error details
- ✅ **Screenshots**: Automatically captures screenshots on failures
- ✅ **Test metadata**: Displays test markers, descriptions, and execution details

## Project Structure

```
Playwright example/
├── rules/
│   ├── Starting Rules.md          # Core project rules
│   └── Testing Rules.md           # Testing-specific rules
├── tests/
│   ├── conftest.py               # Pytest configuration with base URL
│   ├── test_example.py           # Basic tests using base URL
│   └── test_page_objects.py      # Page Object Model tests
├── playwright-report/            # HTML test reports (auto-generated)
│   └── report.html              # Latest test report
├── requirements.txt              # Python dependencies (latest versions)
├── pytest.ini                   # Pytest configuration with HTML reporter
├── playwright.config.ts          # Playwright configuration
├── state.json                   # Example storage state file
├── README.md                    # Project documentation
└── .gitignore                   # Git ignore file
```

## Design Patterns

This project follows official Playwright documentation patterns:

### Page Object Model (POM)
```python
class PlaywrightHomePage:
    def __init__(self, page: Page):
        self.page = page
        self.search_button = page.get_by_role("button", name="Search (Ctrl+K)")
    
    def navigate(self):
        self.page.goto("/")  # Uses base URL
```

### Role-Based Selectors
```python
# Accessibility-first selectors
page.get_by_role("button", name="Search (Ctrl+K)")
page.get_by_role("searchbox", name="Search")
page.get_by_role("link", name="Docs")
```

### Web-First Assertions
```python
# Auto-retrying assertions
expect(page).to_have_title("...")
expect(page.locator("h1")).to_contain_text("...")
expect(search_box).to_have_value("python")
```

## Official Documentation Compliance

This project follows the [official Playwright documentation](https://playwright.dev/docs/test-use-options) for:

- ✅ **Base URL configuration** - Allows using relative URLs
- ✅ **Storage state configuration** - For authentication scenarios
- ✅ **Viewport settings** - Consistent browser window size
- ✅ **HTTP headers** - Custom headers for all requests
- ✅ **HTTPS error handling** - Ignore SSL certificate errors
- ✅ **Browser launch options** - Headless mode, slow motion
- ✅ **Role-based selectors** - Accessibility-first approach
- ✅ **Web-first assertions** - Auto-retrying assertions
- ✅ **Explicit waits** - No sleep() calls

## Best Practices

### Accessibility Testing
- Using role-based selectors for better accessibility
- Following WCAG guidelines for test selectors

### Test Reliability
- Web-first assertions that auto-retry
- Explicit waits instead of sleep()
- Proper test isolation with fresh contexts

### Maintainability
- Page Object Model for UI element management
- Comprehensive commenting throughout code
- Clear test organization and naming

## Troubleshooting

### Common Issues
1. **Browser not found**: Run `playwright install`
2. **Tests failing**: Check if base URL is accessible
3. **Slow tests**: Adjust `slow_mo` in conftest.py

### Debug Mode
```bash
# Run with browser visible and slow motion
pytest --headed --slowmo 2000
```

## Resources

- [Playwright Documentation](https://playwright.dev/)
- [Playwright Python API](https://playwright.dev/python/docs/api/class-playwright)
- [Pytest Documentation](https://docs.pytest.org/)
- [Playwright Best Practices](https://playwright.dev/python/docs/best-practices)
- [Playwright Test Use Options](https://playwright.dev/docs/test-use-options) 