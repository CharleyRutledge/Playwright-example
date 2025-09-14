---
description: 'Instructions for fixing failing tests'
applyTo: '**'
---

# Fixing Failed Tests

## 🎯 Mission

Your mission is to systematically fix failing tests by following a rigorous debugging and verification process.

## 📋 Process

### 1. **Re-run the Failed Test**
- After a test fails unexpectedly, immediately re-run the test
- This helps determine if the failure is consistent or intermittent
- Use verbose output to get detailed error information

### 2. **Debug Until Fixed**
- Don't stop debugging until you have successfully fixed the test
- Analyze error messages, stack traces, and test output
- Check for common issues like locator problems, timing issues, or assertion mismatches

### 3. **Close Browser Context After Success**
- Once the test passes, properly close the browser context
- This ensures clean state for subsequent tests
- Prevents resource leaks and test interference

### 4. **Verify the Fix**
- Re-run the test again to confirm it consistently passes
- This step validates that your fix is robust and not a fluke
- Run the test multiple times if needed to ensure stability

### 5. **Update the Code**
- Commit your fixes to the test code
- Ensure the solution follows best practices
- Add appropriate comments if the fix involves complex logic

### 6. **Update Associated Documentation**
- Update any documentation that references the test or its functionality
- This includes README files, test descriptions, or API documentation
- Ensure documentation reflects the current test behavior and requirements

## 🔧 Best Practices

- **Use verbose output**: Run tests with `-v` flag for detailed information
- **Check error logs**: Review console output and error messages carefully
- **Test isolation**: Ensure fixes don't break other tests
- **Documentation sync**: Keep code and documentation in sync
- **Version control**: Commit fixes with clear, descriptive commit messages

## 🚀 Ready to Fix Tests

I'm ready to help you fix any failing tests. Please run the test suite or specific failing tests, and I'll follow this process to resolve the issues systematically.

