import os
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Dialogflow MCP")

def get_env(key, fallback):
    return os.getenv(key) or fallback

@mcp.tool()
def get_agent_info():
    return {
        "project": get_env("PROJECT_ID", "grow-to-millions-bot"),
        "location": get_env("LOCATION", "asia-south1"),
        "agent": get_env("AGENT_ID", "f21e5fd9-fa5e-464a-a3eb-a0cd3dbed5a9")
    }

app = mcp.streamable_http_app()
