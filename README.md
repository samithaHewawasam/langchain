# LangChain Agent Examples

A collection of LangChain agent examples using AWS Bedrock and Claude Sonnet 4.5.

## Overview

This repository demonstrates how to build AI agents using LangChain with AWS Bedrock's Claude models. It includes examples of:

- Simple function calling with agents
- Web scraping agents with custom tools
- State management with checkpointers

## Project Structure

```
langchagin/
├── code-review-agent/
│   ├── agent.py           # Simple weather agent example
│   ├── agent-tool.py      # Web fetching agent with tools
│   └── .venv/             # Python virtual environment
└── README.md
```

## Prerequisites

- Python 3.13+
- AWS credentials configured for Bedrock access
- Access to Claude Sonnet 4.5 model on AWS Bedrock

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd langchagin
```

2. Create and activate a virtual environment:
```bash
cd code-review-agent
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install langchain langchain-aws langgraph langchain-core requests certifi
```

## Usage

### Simple Agent Example

The `agent.py` file demonstrates a basic agent with a custom function:

```bash
python code-review-agent/agent.py
```

This creates an agent that can respond to weather queries using a mock weather function.

### Web Fetching Agent

The `agent-tool.py` file shows a more advanced agent with web scraping capabilities:

```bash
python code-review-agent/agent-tool.py
```

This agent can fetch and analyze content from URLs, demonstrating:
- Custom tool definition with `@tool` decorator
- In-memory state persistence with checkpointers
- HTTP requests with proper headers and SSL verification

## Features

- **AWS Bedrock Integration**: Uses Claude Sonnet 4.5 via AWS Bedrock
- **Custom Tools**: Examples of creating custom tools for agents
- **State Management**: Demonstrates conversation state persistence
- **Error Handling**: Proper exception handling for API calls

## Model Configuration

Both examples use Claude Sonnet 4.5:
```python
model_id="us.anthropic.claude-sonnet-4-5-20250929-v1:0"
```

## License

[Add your license here]

## Contributing

[Add contribution guidelines here]
