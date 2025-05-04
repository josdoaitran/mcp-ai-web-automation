# Note
Here is some examples that we can use MCP Execution Automation Test to gen-code and run the automation test script via our prompting

## Example 1: Gen Code Selenium - Java - TestNG - Cucumber

Use the my `playwright-mcp-exe-automation`  to navigate to the website `https://www.saucedemo.com`. 
- Ensure that the MCP Server is actively handling the browser automation test to validate its integration. 
- Do not simulate the tests statically or bypass the MCP Server. 
- All interactions must be routed through MCP.

On the login page, execute the following two scenarios:

Scenario 1: Valid Login Enter the username as "standard_user" and the password as "secret_sauce".
Given user can access to home page
When user input the correct credential and Click the Login button.
Then User Verify that:
- The user is redirected to /inventory.html.
- No error message is displayed.
- The login form is no longer visible.
- The inventory page is displayed successfully.


Scenario 2: User login with Locked Out User. Enter the username as "locked _out_user" and the password as "secret_sauce".
Given user can access to home page
When user input the correct credential and Click the Login button.
Then User Verify that:
- The user remains on the login page.
- The login form is still visible.
- The following error message is displayed: "Epic sadface: Sorry, this user has been locked out."
7 After both scenarios are validated:
- Close the browser.

Then, Please help me generate the Python Test framework Code using Playwright with MCP Integration to cover the above scenario.

Generated Java Test Framework using:
- New folder for my project: `example-saucedemo-java-selenium`
- It is a Maven Java project. All generated codes have to follow java project
- TestNG with Cucumber
- Dependencies should be defined in POM.xml with maven project
- Web automation test with Selenium.
- Using Page object model in sub-folder: /pages
- Test will be executed in cucumber /features folder

## Example 2: Gen Code Playwright - Pytest

Use the my `playwright-mcp-exe-automation`  to navigate to the website `https://www.saucedemo.com`. 
- Ensure that the MCP Server is actively handling the browser automation test to validate its integration. 
- Do not simulate the tests statically or bypass the MCP Server. 
- All interactions must be routed through MCP.

On the login page, execute the following two scenarios:

Scenario 1: Valid Login Enter the username as "standard_user" and the password as "secret_sauce".
Given user can access to home page
When user input the correct credential and Click the Login button.
Then User Verify that:
- The user is redirected to /inventory.html.
- No error message is displayed.
- The login form is no longer visible.
- The inventory page is displayed successfully.


Scenario 2: User login with Locked Out User. Enter the username as "locked _out_user" and the password as "secret_sauce".
Given user can access to home page
When user input the correct credential and Click the Login button.
Then User Verify that:
- The user remains on the login page.
- The login form is still visible.
- The following error message is displayed: "Epic sadface: Sorry, this user has been locked out."
7 After both scenarios are validated:
- Close the browser.

Then, Please help me generate the Python Test framework Code using Playwright with MCP Integration to cover the above scenario.

Generated Python Test Framework using:
- New folder for my project: `example-saucedemo-pytest-playwright`
- Pytest
- Dependencies should be defined in requirements.txt
- Web automation test with Playwright.
- Using Page object model in sub-folder: /pages
- Test will be executed in cucumber /features folder

