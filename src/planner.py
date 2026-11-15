from .config import MODEL, get_client
from pydantic import BaseModel

class ResearchPlan(BaseModel):
    research_topic: str
    research_objective: str
    paper_count: int
    keywords: list[str]
    search_queries: list[str]
    steps: list[str]
    expected_output: str

SYSTEM_PROMPT = """
You are the planning component of an
AI Research Assistant Agent.

Your task is to create a structured
scientific research plan.

For every research request:

1. Identify the research topic.
2. Define the research objective.
3. Generate relevant keywords.
4. Generate scientific search queries.
5. Create a logical sequence of research steps.
6. Describe the expected final output.

Use the requested number of papers.

Do not invent scientific papers,
authors, citations, or research findings.

You are only creating a research plan.
Do not claim that research has already
been completed.
"""

from openai import OpenAIError

def create_research_plan(
    research_query: str,
    paper_count: int = 5
) -> ResearchPlan:

    # Validate user input
    if not isinstance(research_query, str):
        raise ValueError("Query must be a string.")

    if not research_query.strip():
        raise ValueError("Research query cannot be empty.")

    if len(research_query) > 2000:
        raise ValueError("Research query is too long.")

    if type(paper_count) is not int or not 1 <= paper_count <= 20:
        raise ValueError("Paper count must be between 1 and 20.")

    # Create user prompt
    user_prompt = f"""
    Research request: {research_query}
    Number of papers: {paper_count}
    """

    try:
        client = get_client()
        # Send request to the LLM
        response = client.responses.parse(
            model=MODEL,
            input=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            text_format=ResearchPlan,
            max_output_tokens=1500
        )

        # Get structured output
        plan = response.output_parsed

        if response.status != "completed" or plan is None:
            raise RuntimeError("The model did not return a complete plan.")

        if plan.paper_count != paper_count:
            raise RuntimeError("Incorrect paper count.")

        if not plan.steps or not plan.search_queries:
            raise RuntimeError("Research plan is incomplete.")

        return plan

    except OpenAIError as error:
        raise RuntimeError(
            "LLM request failed: " + type(error).__name__
        ) from error

