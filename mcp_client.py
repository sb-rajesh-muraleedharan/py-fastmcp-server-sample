from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama

from dotenv import load_dotenv
load_dotenv() 

import asyncio
import os

async def main():
    server_configs = {
        "math": { # Math server configuration
            "command": "python",
            "args": ["my_math_server.py"],
            "transport": "stdio",
            "restart_on_failure": True,
        },
        "weather": { # Weather server configuration
            "url": "http://localhost:8001/mcp",
            "transport": "streaming_http",
            "restart_on_failure": False,
        }
    }

    client = MultiServerMCPClient(server_configs) # type: ignore


    tools=await client.get_tools()
    model = ChatOllama(model="llama3.1:8b")
    agent = create_react_agent(
        model, tools
    )

    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What is the square root of 256?"}]}
    )
    print("Math Response:", math_response['messages'][-1].content)

    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What's the weather like in New York?"}]}
    )
    print("Weather Response:", weather_response['messages'][-1].content)

asyncio.run(main())