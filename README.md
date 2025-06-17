# py-fastmcp-server-sample

This is a sample Python project demonstrating a simple MCP (Model Context Protocol) server using FastMCP.

## Features
- Example MCP server implementation
- Custom math operations
- FastAPI-based server

## Requirements
- Python 3.8+
- [fastmcp](https://pypi.org/project/fastmcp/) (install with `pip install fastmcp`)
- fastapi
- uvicorn

## Installation
1. Clone this repository:
   ```sh
   git clone <repo-url>
   cd py-fastmcp-server-sample
   ```
2. (Optional) Create and activate a virtual environment:
   ```sh
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
To start the MCP server, run:
```sh
python my_math_mcp_server.py
```
Or, if using FastAPI with Uvicorn:
```sh
uvicorn my_math_mcp_server:app --reload
```

## Project Structure
- `main.py` — Example client or entry point
- `my_math_mcp_server.py` — MCP server implementation
- `requirements.txt` — Python dependencies
- `pyproject.toml` — Project metadata

## License
MIT License
