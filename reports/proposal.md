
# Project Proposal — Semester Week 10

## Project Title

AI Research Assistant Agent: An Autonomous Scientific Research Assistant

## Problem Description

Students and researchers spend a lot of time searching for scientific papers, reading articles, comparing research methods, and preparing literature reviews.

Finding relevant and reliable scientific information can be difficult, especially when many papers are available on the same topic.

The AI Research Assistant Agent aims to simplify this process using Large Language Models (LLMs) and autonomous agent technology.

The application will automatically search for scientific papers, extract important information, compare research findings, and generate structured literature reviews.

Unlike a simple chatbot, the agent will plan and execute multiple steps, use external tools, handle errors, and verify information before generating the final answer.

The main goal is to save research time and help users understand scientific literature more efficiently.

## Target Users

The main target users are:

- University students working on assignments and graduation projects.
- Researchers conducting literature reviews.
- Teachers preparing educational materials.
- Graduate students searching for scientific publications.
- Data analysts studying scientific research methods.

## Selected Difficulty

**Level A — Advanced**

The project will implement an autonomous AI agent capable of completing multi-step research tasks.

The system will include:

- Real LLM integration.
- At least three meaningful tools.
- Autonomous task planning.
- State management.
- Multi-step tool execution.
- Error handling and recovery.
- Execution limits.
- Security guardrails.
- Execution logs.
- At least 12 tests, including 4 guardrail scenarios.
- A presentation of a recent scientific research paper.

## Expected Functionality

The AI Research Assistant Agent will provide the following functionality:

1. Accept a research topic or question from the user.
2. Analyze the request and create a research plan.
3. Search for relevant scientific papers.
4. Retrieve paper metadata, including title, authors, publication year, and DOI.
5. Extract abstracts and available paper content.
6. Identify research objectives, methods, datasets, and findings.
7. Compare multiple scientific papers.
8. Generate a structured literature review.
9. Provide references and links to original papers.
10. Save intermediate research results.
11. Detect missing information and adapt the research plan.
12. Handle API errors and unavailable papers.
13. Prevent unauthorized actions and unsafe tool execution.
14. Stop execution when the goal is completed or an execution limit is reached.

## Proposed Functions

### Function 1: create_research_plan()

**Purpose:** Analyze the user's research request and generate a sequence of research steps.

**Input:**
- research_query: str
- paper_count: int

**Expected Output:**
- A structured research plan containing the required steps.

**Dependencies:**
- LLM API
- JSON validation

### Function 2: search_papers()

**Purpose:** Search for scientific publications related to the research topic.

**Input:**
- query: str
- max_results: int

**Expected Output:**
- A list of scientific papers with titles, authors, publication years, identifiers, and URLs.

**Dependencies:**
- OpenAlex API
- requests library

### Function 3: get_paper_details()

**Purpose:** Retrieve detailed metadata and available abstracts for a selected scientific paper.

**Input:**
- paper_id: str

**Expected Output:**
- A dictionary containing the paper title, authors, abstract, publication year, DOI, and available source information.

**Dependencies:**
- OpenAlex API
- requests library

### Function 4: extract_paper_content()

**Purpose:** Extract readable text from an accessible scientific paper.

**Input:**
- paper_url: str

**Expected Output:**
- Extracted text or a structured error message if the document cannot be accessed.

**Dependencies:**
- requests library
- PyMuPDF
- PDF validation

### Function 5: analyze_paper()

**Purpose:** Identify important information from a scientific paper.

**Input:**
- paper_text: str
- research_question: str

**Expected Output:**
- Research objective.
- Methodology.
- Dataset or participants.
- Main findings.
- Limitations.

**Dependencies:**
- LLM API
- Structured JSON output
- Source validation

### Function 6: compare_papers()

**Purpose:** Compare multiple scientific publications based on their methods and findings.

**Input:**
- analyzed_papers: list

**Expected Output:**
- A structured comparison table showing similarities, differences, methods, findings, and limitations.

**Dependencies:**
- LLM API
- pandas library

### Function 7: generate_literature_review()

**Purpose:** Generate a structured literature review based on analyzed scientific papers.

**Input:**
- research_topic: str
- analyzed_papers: list

**Expected Output:**
- Introduction.
- Overview of selected studies.
- Comparison of methodologies.
- Main findings.
- Research gaps.
- Conclusion.
- References.

**Dependencies:**
- LLM API
- Citation validation

### Function 8: validate_references()

**Purpose:** Verify that references in the generated report correspond to retrieved scientific publications.

**Input:**
- references: list
- retrieved_papers: list

**Expected Output:**
- Validated references.
- Missing or unsupported citation warnings.

**Dependencies:**
- Paper metadata
- DOI and identifier matching

### Function 9: save_research_state()

**Purpose:** Store intermediate research results and execution progress.

**Input:**
- session_id: str
- state: dict

**Expected Output:**
- Confirmation that the research state was saved successfully.

**Dependencies:**
- JSON
- Local file storage

### Function 10: execute_research_agent()

**Purpose:** Coordinate the complete autonomous research workflow.

**Input:**
- user_request: str

**Expected Output:**
- Final research report.
- Retrieved references.
- Execution summary.
- Error and warning information.

**Dependencies:**
- LLM API
- Agent tools
- State management
- Guardrails
- Execution limits

## Proposed Agent Tools

The agent will use four main LLM-callable tools.

### Tool 1: search_papers

Searches scientific databases for relevant publications.

The agent needs this tool to discover papers related to the user's research question.

### Tool 2: get_paper_details

Retrieves detailed metadata and available abstracts.

The agent needs this tool to examine selected papers before analysis.

### Tool 3: extract_paper_content

Extracts readable content from accessible PDF documents.

The agent needs this tool to obtain additional information beyond abstracts.

### Tool 4: compare_papers

Creates structured comparisons of analyzed studies.

The agent needs this tool to organize findings and identify similarities and differences.

The LLM will select appropriate tools based on the current research goal.

Tool arguments will be validated before execution.

The system will reject invalid or unauthorized tool calls.

## Model Selection

**Proposed LLM:** OpenAI GPT-4o-mini

**Integration Method:** OpenAI API using Python.

**Programming Language:** Python 3.11+

**Main Libraries:**

- openai — LLM integration and tool calling.
- requests — API communication.
- pandas — structured data processing.
- PyMuPDF — PDF text extraction.
- pydantic — input and output validation.
- pytest — automated testing.
- python-dotenv — environment variable management.

**Scientific Data Source:** OpenAlex API.

The OpenAI API key will be stored in an environment variable and will not be uploaded to GitHub.

The selected model may be changed during development if necessary.

## Architecture

The system will follow a multi-step autonomous agent architecture.

```text
                USER
                 |
                 v
         Research Request
                 |
                 v
          Input Validation
                 |
                 v
           LLM Planner
                 |
                 v
          Research Plan
                 |
                 v
          Agent Controller
                 |
       +---------+---------+
       |         |         |
       v         v         v
    Search     Retrieve   Extract
    Papers     Details    PDF Text
       |         |         |
       +---------+---------+
                 |
                 v
          Analyze Papers
                 |
                 v
          Compare Papers
                 |
                 v
        Validate References
                 |
                 v
       Generate Literature
             Review
                 |
                 v
          Final Report
```

### State Management

The agent will maintain a research state containing:

- User request.
- Current research plan.
- Completed steps.
- Retrieved papers.
- Extracted information.
- Tool execution results.
- Errors and warnings.
- Remaining execution budget.

The state will be updated after each step.

### Planning and Adaptation

The agent will generate an initial plan and select tools according to the task.

If a paper is unavailable, the agent may search for another relevant publication.

If a tool fails, the agent will record the error and retry within defined limits or continue with available information.

The agent will stop when the research goal is completed, a critical error occurs, or the execution limit is reached.

### Guardrails

The system will implement:

1. Tool allowlisting.
2. Input and argument validation.
3. Maximum execution steps.
4. API request timeouts.
5. Safe PDF processing.
6. Protection against prompt injection.
7. Citation verification.
8. Protection of API keys and sensitive information.
9. Restrictions on file access.
10. Execution logging without exposing secrets.

## Example Requests

### Example 1

**User Request:**

"Find five scientific papers about adaptive learning in mathematics and compare their research methods."

**Expected Behavior:**

The agent searches for papers, retrieves metadata, analyzes available information, compares methodologies, and generates a structured comparison.

### Example 2

**User Request:**

"Find recent scientific papers about machine learning in education and prepare a literature review."

**Expected Behavior:**

The agent creates a research plan, searches for relevant publications, analyzes selected studies, validates references, and generates a literature review.

### Example 3

**User Request:**

"Compare research papers about student performance prediction and identify the most commonly used machine learning algorithms."

**Expected Behavior:**

The agent retrieves relevant studies, extracts algorithm information, compares methods, and summarizes the findings with references.

## Evaluation Plan

The system will be evaluated using automated tests and practical research tasks.

At least 12 tests will be implemented.

### Functional Tests

**Test 1: Valid Research Request**

Verify that the agent accepts a valid research topic.

**Test 2: Research Planning**

Verify that the agent creates a structured multi-step plan.

**Test 3: Paper Search**

Verify that the search tool returns valid paper metadata.

**Test 4: Paper Details**

Verify that the agent retrieves information about a selected publication.

**Test 5: PDF Extraction**

Verify that the system extracts text from an accessible PDF.

**Test 6: Paper Analysis**

Verify that the system produces structured information from available paper content.

**Test 7: Paper Comparison**

Verify that the system compares multiple studies correctly.

**Test 8: Error Recovery**

Simulate an unavailable paper or API failure and verify that the agent handles the problem appropriately.

### Guardrail Tests

**Test 9: Unauthorized Tool Call**

Verify that the agent rejects tools outside the approved tool list.

**Test 10: Prompt Injection**

Insert malicious instructions into retrieved paper content and verify that the agent ignores them.

**Test 11: Execution Limit**

Verify that the agent stops after reaching the maximum permitted number of steps.

**Test 12: Unsafe File Access**

Verify that the agent rejects unauthorized local file paths and unsafe document access.

### Additional Tests

**Test 13: Invalid Input**

Verify that empty or invalid research requests are rejected.

**Test 14: Citation Validation**

Verify that the system identifies unsupported or missing references.

### Evaluation Metrics

The following metrics will be recorded:

- Task completion rate.
- Tool execution success rate.
- Reference validation accuracy.
- Number of completed research steps.
- Error recovery success.
- Guardrail test pass rate.
- Total execution time.

The agent will be evaluated using controlled examples and a small set of real scientific research questions.

## Weekly Milestones

### Week 10 — November 2–8, 2026

**Proposal and Planning**

- Select the project topic.
- Define the problem and target users.
- Choose difficulty level A.
- Identify the main functions.
- Define agent tools.
- Design the system architecture.
- Prepare the evaluation plan.
- Create the project proposal.

**Deliverable:** reports/proposal.md

### Week 11 — November 9–15, 2026

**Initial LLM Integration**

- Set up the Python environment.
- Install required libraries.
- Configure the OpenAI API.
- Implement the first LLM request.
- Create the initial research planning function.
- Document the setup process.

**Deliverable:** Initial LLM-powered prototype.

### Week 12 — November 16–22, 2026

**Core Functionality**

- Implement research request validation.
- Implement scientific paper search.
- Retrieve paper metadata.
- Introduce structured JSON outputs.
- Add initial unit tests.

**Deliverable:** Working core application.

### Week 13 — November 23–29, 2026

**Tool Integration**

- Implement at least three agent tools.
- Register tools for LLM function calling.
- Validate tool arguments.
- Demonstrate dynamic tool selection.
- Record tool execution results.

**Deliverable:** Integrated agent tools.

### Week 14 — November 30–December 6, 2026

**Autonomous Agent Workflow**

- Implement multi-step execution.
- Add research state management.
- Implement conditional planning.
- Define stopping conditions.
- Demonstrate an end-to-end research workflow.
- Select a recent scientific paper for the required presentation.

**Deliverable:** Autonomous research workflow and paper selection.

### Week 15 — December 7–13, 2026

**Reliability and Guardrails**

- Add execution limits.
- Implement tool permission checks.
- Add prompt injection protection.
- Improve API error handling.
- Test recovery behavior.
- Record execution traces.

**Deliverable:** Reliability and guardrail test results.

### Week 16 — December 14–20, 2026

**Evaluation and Improvement**

- Run at least 12 tests.
- Complete four mandatory guardrail scenarios.
- Record test results.
- Analyze system failures.
- Improve agent reliability.
- Update documentation.
- Prepare the research paper presentation.

**Deliverable:** reports/week-16.md and evaluation results.

### Week 17 — December 21–22, 2026

**Final Submission and Defense**

- Complete the application.
- Finalize the README.
- Submit all required weekly reports.
- Prepare the final project report.
- Submit the GitHub repository URL.
- Submit the final commit hash.
- Demonstrate autonomous agent execution.
- Present the selected scientific paper.
- Explain the architecture, tools, testing, and guardrails.

**Deliverable:** Complete A-level AI Research Assistant Agent.



