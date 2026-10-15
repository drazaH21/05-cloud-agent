# 05-Cloud-Agent: Enterprise Tool-Use Agent

A production-grade, extensible AI agent built with **Python**, **Groq**, and **Pydantic**, featuring native function calling (tool-use) for dynamic enterprise data retrieval, metric calculation, and synthesized executive responses.

## Architecture

```text
[User Query]
     │
     ▼
[Groq Agent Core] ─── (Native Function Calling / Tool Selection)
     │
     ├─────────► [Tool: get_enterprise_metric] ───► (Backend Datastore Lookup)
     │
     ▼
[Final Synthesis & Structured Output]
```

## Key Components

- **Agent Core (`src/agent.py`)**: Manages conversational message history, handles Groq API multi-turn execution loops, and parses tool requests.
- **Enterprise Tools (`src/tools.py`)**: Exposes backend function schemas for automated metrics lookup (e.g., P&L bridges, global revenue pipelines, and retention heuristic scores).
- **Execution Model**: Powered by high-speed LPU acceleration (`openai/gpt-oss-20b`) with strict tool schema validation.

## Quick Start

1. Clone the repository and navigate into the folder.
2. Create and activate your virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
4. Create a `.env` file and configure your API key:
   ```env
   GROQ_API_KEY=your_actual_groq_api_key_here
   ```
5. Run the test script:
   ```powershell
   python -m tests.test_agent
   ```