## Test case 1001 implement reporter
#Scenario: If I don't have the playwright HMTL reporter implemented, implement it.
Test steps: 
1. open the playwright documents
2. Find the HTML reporter section
3. validate the URL matches https://playwright.dev/docs/test-reporters
4. Implement the HTML reporter in this project
5. if the test are finished running,Save the results and automatically run the HTML reporter.

## Rules
- Rule 1: Ensure the rules defined in `rules/Starting Rules.md` are followed.
- Rule 2: Ensure the rules defined in `rules/Testing Rules.md` are followed.
- Rule 3: Use pytest-playwright not the native Playwright test runner and if 
the @playwright/test module isn't installed,install it.
- Rule 4: if a report already exists, delete it and replace it with the new one.
