# mcp-web-automation-playwright-cursor
- Let start with a mcp for covering web-automation with playwright in cursor.
- It is based on: MCP Execution Playwright, Cursor

## MCP - ExecuteAutomation
- https://github.com/executeautomation/mcp-playwright
- A Model Context Protocol server that provides browser automation capabilities using Playwright. This server enables LLMs to interact with web pages, take screenshots, generate test code, web scraps the page and execute JavaScript in a real browser environment.

## Cursor AI Editor.
- Modern Editor tool - Core VSCode: https://www.cursor.com/
- MCP feature in Cursor: https://docs.cursor.com/context/model-context-protocol

The Model Context Protocol (MCP) is an open protocol that standardizes how applications provide context and tools to LLMs. Think of MCP as a plugin system for Cursor - it allows you to extend the Agent’s capabilities by connecting it to various data sources and tools through standardized interfaces.

# Setup the local environment
- Install MCP Playwright from ExecutionAutomation:
```cmd
npm install -g @executeautomation/playwright-mcp-server
```
In cases, you get the troubles in install some dependencies in node. You can run these command:
```
❯ sudo chown -R $(whoami) ~/.npm
❯ sudo chown -R $(whoami) /usr/local/lib/node_modules/npm/node_modules
```
- Install Python
- Configure Virtual Python in this project.
```
# Set up virtual environment
python -m venv venv
# On MacOSX / Linux
source venv/bin/activate  
# On Windows: venv\Scripts\activate
```