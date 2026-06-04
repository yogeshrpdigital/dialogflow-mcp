from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Dialogflow MCP")

@mcp.tool()
def hello():
    return "Hello from MCP"

if __name__ == "__main__":
    mcp.run()