from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq

from dotenv import load_dotenv
load_dotenv() 

import asyncio
import os

async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["my_math_server.py"],
                "transport": "stdio",
                "restart_on_failure": True,
            },
            "weather": {
                "url": "http://localhost:8001/mcp",
                "transport": "streaming_http",
                "restart_on_failure": False,
            }
        })
    
    os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

    tools=await client.get_tools()
    model=ChatGroq(model="qwen-qwq-32b")
    agent = create_react_agent(
        model, tools, verbose=True
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