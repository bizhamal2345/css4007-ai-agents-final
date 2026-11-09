
# Week 10 Progress Report

## Completed Work

During Week 10, I worked on the initial planning and design of my AI Research Assistant Agent project.

The following planning tasks were completed:

1. Selected the project topic: AI Research Assistant Agent.
2. Selected Level A (Advanced) as the target difficulty.
3. Defined the main problem and target users.
4. Identified the expected application functionality.
5. Designed a preliminary autonomous agent architecture.
6. Proposed the main Python functions and agent tools.
7. Selected Python and the OpenAI API as the proposed technologies.
8. Designed an evaluation plan with 14 test scenarios.
9. Prepared weekly development milestones from Week 10 to Week 17.
10. Prepared the initial project proposal.

The main objective is to develop an autonomous AI agent that can search for scientific papers, analyze research findings, compare publications, and generate structured literature reviews.

## Important Commits

### Commit 1

- **Commit hash:** TODO - Add actual commit hash
- **Description:** Added the initial project proposal for the AI Research Assistant Agent.
- **Link:** TODO - Add actual GitHub commit URL

### Commit 2 (if applicable)

- **Commit hash:** TODO - Add actual commit hash, or remove this entry
- **Description:** Added or updated the Week 10 progress report.
- **Link:** TODO - Add actual GitHub commit URL, or remove this entry

## Current Functionality

The project is currently in the planning and design stage.

The proposed system architecture and main components have been defined.

The planned agent will be able to:

- Accept scientific research questions.
- Generate multi-step research plans.
- Search for scientific publications.
- Retrieve paper metadata and available content.
- Analyze research methods and findings.
- Compare multiple scientific studies.
- Generate structured literature reviews.
- Validate references.
- Save research progress.
- Handle errors and execution limits.

These capabilities are planned and have not yet been implemented.

## Problems Encountered

The main challenges during project planning were:

1. Defining a realistic project scope for Level A.
2. Understanding the difference between a basic LLM application and an autonomous AI agent.
3. Selecting meaningful tools for scientific research.
4. Designing a workflow that can handle unavailable papers and API failures.
5. Planning how to prevent incorrect or unsupported references.

## Solutions

To address these challenges, I made the following design decisions:

1. Focused the project on scientific paper search, analysis, comparison, and literature review generation.
2. Designed a multi-step workflow with planning, tool execution, and state management.
3. Proposed OpenAlex as the scientific publication data source.
4. Selected four tools: search_papers, get_paper_details, extract_paper_content, and compare_papers.
5. Included citation validation and error recovery in the proposed architecture.
6. Planned execution limits and security guardrails.
7. Defined 14 test scenarios, including four guardrail tests.

These are design decisions that will be implemented and tested during the following weeks.

## What I Learned

During the project planning stage, I learned the basic concepts of autonomous AI agents.

I learned that an LLM is a language model that processes text and generates responses.

An AI agent uses an LLM together with tools, planning, and state management to complete tasks.

I also learned that tool calling allows the model to select functions based on the user's request.

State management helps the agent remember intermediate results and track completed steps.

Guardrails are safety mechanisms that restrict unauthorized actions and control execution.

I understood that an Advanced-level AI agent must demonstrate real multi-step execution, not only generate text.

## Next Week

During Week 11, I plan to:

1. Set up the Python development environment.
2. Install the required libraries.
3. Configure the OpenAI API.
4. Store the API key securely using environment variables.
5. Implement the first working LLM request.
6. Create the initial research planning function.
7. Test basic LLM communication.
8. Add setup instructions to the project documentation.
9. Commit the working prototype to GitHub.

**Expected Deliverable:** Initial LLM-powered prototype of the AI Research Assistant Agent.
