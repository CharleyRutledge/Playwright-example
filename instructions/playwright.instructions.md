---
description: 'Comprehensive Playwright test writing guidelines for Python and pytest'
applyTo: '**'
---

# Comprehensive Playwright Test Writing Guidelines for Python

## 🎯 **Overview**

This document provides comprehensive guidelines for writing Playwright tests using Python and pytest-playwright. These guidelines ensure tests are maintainable, accessible, and follow Python best practices.

## 🐍 **Python & Pytest Fundamentals**

### **Required Imports**
```python
import pytest
from playwright.sync_api import Page, expect
from typing import Any, Optional
```

### **Project Structure**
```
tests/
├── __init__.py
├── conftest.py
├── test_shop.py
├── test_contact_form.py
├── test_promotions.py
└── test_*.py
```

### **Test File Naming Convention**
- Use `test_<feature_or_page>.py` format
- Examples: `test_shop.py`, `test_login.py`, `test_checkout.py`
- Store all test files in the `tests/` directory

## 🔧 **Code Quality Standards**

### **Locator Strategy (Priority Order)**
1. **`get_by_role()`** - Most accessible and resilient
   ```python
   page.get_by_role("button", name="Add to cart")
   page.get_by_role("link", name="Home")
   page.get_by_role("textbox", name="Username")
   ```

2. **`get_by_label()`** - For form inputs with labels
   ```python
   page.get_by_label("Email Address")
   page.get_by_label("Password")
   ```

3. **`get_by_text()`** - For text content (use `.first` or `.nth()` for multiple matches)
   ```python
   page.get_by_text("Submit").first
   page.get_by_text("*").nth(1)
   ```

4. **`get_by_test_id()`** - For specific test identifiers
   ```python
   page.get_by_test_id("add-to-cart-button")
   ```

### **Assertion Best Practices**
- Use Playwright's built-in assertions with proper Python syntax
- These assertions are web-first and auto-retrying
- Avoid hard-coded waits or increased timeouts

```python
# Element visibility and state
expect(locator).to_be_visible()
expect(locator).to_be_hidden()
expect(locator).to_be_enabled()
expect(locator).to_be_disabled()

# Text content
expect(locator).to_have_text("Exact text match")
expect(locator).to_contain_text("Partial text match")
expect(locator).to_have_value("input value")

# Element attributes and counts
expect(locator).to_have_attribute("href", "https://example.com")
expect(locator).to_have_count(3)

# Page-level assertions
expect(page).to_have_title("Page Title")
expect(page).to_have_url("https://example.com/page")
```

### **Timeouts and Waiting**
- Rely on Playwright's built-in auto-waiting mechanisms
- Avoid `page.wait_for_timeout()` or hard-coded waits
- Use `expect().to_be_visible()` for dynamic content

## 🏗️ **Test Structure and Organization**

### **Class-Based Organization**
```python
import pytest
from playwright.sync_api import Page, expect

class TestShopFunctionality:
    """Test suite for shop-related functionality."""
    
    @pytest.fixture(autouse=True)
    def setup(self, page: Page) -> None:
        """Navigate to shop page before each test."""
        page.goto("https://demos.bellatrix.solutions/shop/")
    
    def test_display_shop_homepage(self, page: Page) -> None:
        """Test that shop homepage displays correctly."""
        # Test implementation here
        expect(page.get_by_role("heading", level=1)).to_be_visible()
    
    def test_add_product_to_cart(self, page: Page) -> None:
        """Test adding a product to the shopping cart."""
        # Test implementation here
        pass
```

### **Test Method Naming Convention**
- Use `test_<description>` format
- Be descriptive and specific
- Use snake_case for method names

```python
def test_display_contact_form_correctly(self, page: Page) -> None:
def test_handle_form_validation_correctly(self, page: Page) -> None:
def test_display_promotions_page_correctly(self, page: Page) -> None:
```

### **Docstrings and Documentation**
- Add docstrings to all test methods
- Explain complex logic or non-obvious interactions
- Document expected behavior and test purpose

## 🎭 **Advanced Testing Patterns**

### **Parameterized Tests**
```python
@pytest.mark.parametrize("product_name", [
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Bolt T-Shirt"
])
def test_add_different_products_to_cart(self, page: Page, product_name: str) -> None:
    """Test adding different products to cart."""
    # Test implementation here
    pass
```

### **Custom Fixtures**
```python
@pytest.fixture
def logged_in_user(page: Page) -> None:
    """Login fixture for authenticated tests."""
    page.goto("/login")
    page.get_by_label("Username").fill("standard_user")
    page.get_by_label("Password").fill("secret_sauce")
    page.get_by_role("button", name="Login").click()

@pytest.fixture
def cart_with_items(page: Page) -> None:
    """Setup cart with test items."""
    # Add items to cart
    pass
```

### **Test Markers**
```python
@pytest.mark.slow
def test_complex_workflow(self, page: Page) -> None:
    """Test complex user workflow (marked as slow)."""
    pass

@pytest.mark.skip(reason="Feature not yet implemented")
def test_future_feature(self, page: Page) -> None:
    """Test for feature that will be implemented later."""
    pass

@pytest.mark.xfail(reason="Known issue to be fixed")
def test_known_broken_feature(self, page: Page) -> None:
    """Test for feature with known issues."""
    pass
```

## 🚀 **Test Execution Strategy**

### **Basic Commands**
```bash
# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_shop.py

# Run specific test method
pytest tests/test_shop.py::TestShopFunctionality::test_display_shop_homepage

# Run with verbose output
pytest tests/ -v

# Run with headed browser (visible)
pytest tests/ --headed

# Run with headless browser (hidden)
pytest tests/ --headless
```

### **Advanced Commands**
```bash
# Run tests in parallel
pytest tests/ -n auto

# Run tests with retry on failure
pytest tests/ --reruns 3

# Run tests with specific browser
pytest tests/ --browser=firefox

# Run tests with coverage
pytest tests/ --cov=tests --cov-report=html

# Run tests with specific markers
pytest tests/ -m "not slow"

# Run tests with short traceback
pytest tests/ --tb=short
```

### **Debugging Commands**
```bash
# Run with debugger on failure
pytest tests/ --pdb

# Run with maximum verbosity
pytest tests/ -vvv

# Run single test with debug output
pytest tests/test_shop.py::TestShopFunctionality::test_display_shop_homepage -s
```

## 📋 **Quality Checklist**

Before finalizing tests, ensure:

- [ ] All locators are accessible and avoid strict mode violations
- [ ] Tests are grouped logically in classes and follow clear structure
- [ ] Assertions are meaningful and reflect user expectations
- [ ] Tests follow consistent naming conventions (snake_case)
- [ ] Code is properly formatted with proper Python syntax
- [ ] Docstrings are added for complex methods
- [ ] Type hints are used where appropriate
- [ ] Tests handle edge cases and error conditions
- [ ] Tests are independent and can run in any order
- [ ] No hard-coded waits or timeouts are used

## 🔍 **Common Patterns and Examples**

### **Form Testing**
```python
def test_contact_form_submission(self, page: Page) -> None:
    """Test contact form submission functionality."""
    # Fill form fields
    page.get_by_label("Name").fill("Test User")
    page.get_by_label("Email").fill("test@example.com")
    page.get_by_label("Message").fill("Test message")
    
    # Submit form
    page.get_by_role("button", name="Send Message").click()
    
    # Verify success
    expect(page.get_by_text("Message sent successfully")).to_be_visible()
```

### **Navigation Testing**
```python
def test_navigation_between_pages(self, page: Page) -> None:
    """Test navigation between different pages."""
    # Navigate to page
    page.get_by_role("link", name="Contact").click()
    
    # Verify navigation
    expect(page).to_have_url("https://demos.bellatrix.solutions/contact-form/")
    expect(page.get_by_role("heading", level=1)).to_contain_text("Contact")
```

### **Dynamic Content Testing**
```python
def test_dynamic_content_loading(self, page: Page) -> None:
    """Test dynamic content loading and display."""
    # Wait for content to load
    expect(page.get_by_role("list", name="products")).to_be_visible()
    
    # Verify content
    product_items = page.get_by_role("listitem")
    expect(product_items).to_have_count(6)
```

## 🛠️ **Troubleshooting Common Issues**

### **Strict Mode Violations**
```python
# ❌ Bad - Multiple elements found
page.get_by_text("*").click()

# ✅ Good - Specific element selection
page.get_by_text("*").first.click()
page.get_by_text("*").nth(1).click()
```

### **Timing Issues**
```python
# ❌ Bad - Hard-coded wait
page.wait_for_timeout(2000)

# ✅ Good - Wait for element
expect(page.get_by_role("button", name="Submit")).to_be_visible()
```

### **Locator Issues**
```python
# ❌ Bad - CSS selector
page.locator(".btn-primary").click()

# ✅ Good - Role-based locator
page.get_by_role("button", name="Submit").click()
```

## 📚 **Additional Resources**

- [Playwright Python Documentation](https://playwright.dev/python/)
- [Pytest Documentation](https://docs.pytest.org/)
- [Pytest-Playwright Documentation](https://pytest-playwright.readthedocs.io/)
- [Python Testing Best Practices](https://docs.pytest.org/en/stable/goodpractices.html)
- [Playwright Locators Guide](https://playwright.dev/python/docs/locators)
- [Playwright Assertions Guide](https://playwright.dev/python/docs/assertions)

## 🎯 **Best Practices Summary**

1. **Use accessibility-first locators** (`get_by_role`, `get_by_label`)
2. **Organize tests in logical classes** with descriptive names
3. **Use pytest fixtures** for setup and teardown
4. **Write meaningful assertions** that reflect user expectations
5. **Follow Python naming conventions** (snake_case)
6. **Add comprehensive docstrings** for complex logic
7. **Use type hints** where appropriate
8. **Avoid hard-coded waits** and rely on Playwright's auto-waiting
9. **Test user workflows** rather than implementation details
10. **Maintain test independence** and avoid test coupling
