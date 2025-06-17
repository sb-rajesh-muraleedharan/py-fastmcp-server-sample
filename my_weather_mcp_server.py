from fastmcp import FastMCP

mcp = FastMCP("My simple weather MCP server")

@mcp.tool
def get_current_weather(location: str) -> dict:
    """Get the current weather for a specific location"""
    # Simulate a weather API response
    return {
        "location": location,
        "temperature": 72,
        "condition": "Sunny"
    }

@mcp.tool
def get_weather_forecast(location: str) -> list:
    """Get the weather forecast for the next few days"""
    # Simulate a weather API response
    return [
        {"day": "Monday", "temperature": 70, "condition": "Cloudy"},
        {"day": "Tuesday", "temperature": 75, "condition": "Sunny"},
        {"day": "Wednesday", "temperature": 68, "condition": "Rainy"},
    ]

if __name__ == "__main__":
    mcp.run(transport="streamable-http")