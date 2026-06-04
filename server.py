from mcp.server.fastmcp import FastMCP
import uvicorn
import os

mcp = FastMCP("Dialogflow MCP")

@mcp.tool()
def hello():
    return "Hello from MCP Server"

app = mcp.streamable_http_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
