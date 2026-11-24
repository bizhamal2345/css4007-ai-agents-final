# Week 12 Progress Report

## Completed Work

The focus of Week 12 was the implementation
of the core functionality of the AI Research
Assistant Agent.

The implementation includes:

- OpenAlex API integration.
- Scientific paper search functionality.
- Structured paper models using Pydantic.
- Scientific paper metadata extraction.
- Abstract reconstruction.
- Input and output validation.
- Duplicate paper detection.
- API error handling.
- CSV and JSON export in the demonstration notebook.
- Integration with the LLM research planner.
- Eight initial automated test scenarios.

## Important Commits

- Commit hash: TODO
- Description: Added the structured
  scientific paper model.
- Link: TODO

- Commit hash: TODO
- Description: Implemented OpenAlex
  paper search and validation.
- Link: TODO

- Commit hash: TODO
- Description: Connected the research
  planner with scientific paper search.
- Link: TODO

- Commit hash: TODO
- Description: Added eight automated
  unit tests.
- Link: TODO

## Current Functionality

The application is designed to accept
a scientific research topic and generate
a structured research plan using an LLM.

The paper search component retrieves
scientific publications from OpenAlex.

The returned information includes:

- Paper title.
- Authors.
- Publication year.
- DOI.
- Citation count.
- Available abstract.
- Publication URL.
- Available PDF URL.

The application validates input data,
processes API responses, and removes
duplicate publications.

The demonstration notebook also supports
CSV and JSON export.

Live API verification result: TODO

Number of papers retrieved: TODO

Automated test results: TODO

The current workflow uses predefined
function calls. Autonomous LLM tool
selection will be implemented later.

## Problems Encountered

The main technical challenges considered
during implementation were:

- Processing OpenAlex API responses.
- Reconstructing scientific abstracts.
- Handling missing paper metadata.
- Preventing duplicate publications.
- Handling API failures.
- Testing external API functionality.

Actual problems encountered during
execution: TODO

## Solutions

The application uses Pydantic models
to validate scientific paper metadata.

A dedicated function reconstructs text
from abstract inverted indexes.

Missing optional information is handled
without stopping the entire search process.

Duplicate papers are detected using
OpenAlex identifiers and DOI values.

API requests have a timeout and basic
exception handling.

Mock API responses are used in automated
tests to make test execution reproducible.

## What I Learned

I learned how external scientific APIs
can be integrated into an AI application.

I studied how to retrieve scientific
publication metadata and transform
JSON responses into structured Python objects.

I also learned about input validation,
duplicate detection, exception handling,
and automated unit testing.

I understood the importance of separating
LLM-generated research plans from
real scientific information retrieved
through external tools.

## Next Week

During Week 13, I plan to:

- Register scientific research functions
  as LLM-callable tools.
- Implement the paper details tool.
- Implement the PDF extraction tool.
- Validate tool arguments.
- Demonstrate dynamic LLM tool selection.
- Define tool permission policies.
- Start multi-step tool orchestration.
- Record tool execution results.

Expected deliverable:

An integrated AI research prototype
with at least three functional tools.


