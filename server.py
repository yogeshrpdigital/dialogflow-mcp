from mcp.server.fastmcp import FastMCP
from mcp.server.fastmcp.settings import Settings, TransportSecuritySettings
import uvicorn
import os

settings = Settings(
    transport_security=TransportSecuritySettings(
        enable_dns_rebinding_protection=False
    )
)

mcp = FastMCP(
    "Dialogflow MCP",
    settings=settings
)

@mcp.tool()
def hello():
    return "Hello from MCP Server"

app = mcp.streamable_http_app()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)
