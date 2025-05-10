# mcp-web-automation-playwright-microsoft
- Let start with a mcp for covering web-automation with playwright in Vscode - Copilot and Claude
- It is based on: MCP Microsoft Playwright

# MCP - Playwright Microsoft
- [MCP Playwright Microsoft]](https://github.com/microsoft/playwright-mcp)
- A Model Context Protocol (MCP) server that provides browser automation capabilities using Playwright. This server enables LLMs to interact with web pages through structured accessibility snapshots, bypassing the need for screenshots or visually-tuned models.
- Work with LLM via tools: Claude AI, VSCode Copilot, Cursor

# Installation MCP Playwright
- NodeJS
- Install MCP Playwright via this command
```terminal
npm install -g @playwright/mcp@latest
```

In cases, you get the troubles in install some dependencies in node. You can run these command:
```
sudo chown -R $(whoami) /usr/local/lib/node_modules
sudo chown -R $(whoami) /usr/local/bin
Password:
npm install -g @playwright/mcp@latest

added 86 packages in 1s

16 packages are looking for funding
  run `npm fund` for details
```

# Configure MCP

Configure via this configuration value:

```json
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest"
      ]
    }
  }
}
```

# References
- [MCP Playwright Microsoft]](https://github.com/microsoft/playwright-mcp)