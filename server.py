from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Dialogflow MCP")

@mcp.tool()
def health():
    return {"status": "ok"}

app = mcp.streamable_http_app()

