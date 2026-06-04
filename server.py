import os
from mcp.server.fastmcp import FastMCP
from mcp.server.transport_security import TransportSecuritySettings

def require_env(key: str):
    value = os.getenv(key)
    if not value:
        raise ValueError(f"Missing env var: {key}")
    return value

mcp = FastMCP(
    "Dialogflow MCP",
    transport_security=TransportSecuritySettings(
        enable_dns_rebinding_protection=False,
        allowed_hosts=[],
        allowed_origins=[]
    )
)

@mcp.tool()
def get_agent_info():
    return {
        "project": require_env("PROJECT_ID"),
        "location": require_env("LOCATION"),
        "agent": require_env("AGENT_ID")
    }

@mcp.tool()
def health():
    return {"status": "ok"}

app = mcp.streamable_http_app()
