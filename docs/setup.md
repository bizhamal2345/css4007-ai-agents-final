
# AI Research Assistant — Setup

## Current Version

Week 11: Initial LLM Integration.

## Requirements

- Python 3.11 or later
- OpenAI API key

## Installation

Install the required dependencies:

    pip install -r requirements.txt

Create a .env file based on .env.example.

Add your OpenAI API key to the .env file.

## Run the Application

From the repository root, execute:

    python -m src.main

Enter a scientific research topic and
the desired number of papers.

## Current Functionality

- OpenAI API integration
- Research planning
- Structured output
- Input validation
- Basic error handling

## Limitations

The current prototype only generates research plans.

Scientific paper retrieval, tool execution,
and autonomous workflows will be implemented
in later development stages.
