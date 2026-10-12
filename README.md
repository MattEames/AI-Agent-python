# AI Agent in Python

An extensible, tool-calling AI coding agent built in Python using the OpenAI SDK and routed through [OpenRouter](https://openrouter.ai/). 

The agent runs inside a safe execution loop, allowing it to inspect directory structures, read file contents, modify/write files, and execute Python scripts iteratively until it fulfills the user's request.

---

## Features

- **Automated Tool Calling**: Uses OpenAI-compatible tool/function schemas to inspect and interact with the local workspace.
- **Iterative Execution Loop**: Processes multi-step tasks in an assistant-tool loop (up to 20 iterations) until completion.
- **Built-in Security Guardrails**:
  - Validates and restricts all file operations (`read`, `write`, `list`, `execute`) strictly inside a designated sandbox directory (e.g., `./calculator`).
  - Protects against directory traversal attacks (`../`, `/bin`, etc.).
  - Enforces character limits on file reads to prevent prompt context bloat.
- **CLI Options**: Supports verbose logging (`--verbose`) to inspect token usage, intermediate tool calls, and execution outputs step-by-step.

---

## Tool Capabilities

The agent is equipped with the following custom tools defined in `functions/`:

1. `get_files_info`: Lists files and directories with size and metadata.
2. `get_file_content`: Reads text files safely up to `MAX_CHARS` (configurable in `config.py`).
3. `write_file`: Writes or overwrites text files while automatically creating parent directories.
4. `run_python_file`: Safely executes Python scripts via `subprocess` with optional arguments and timeout protection.

---

## Directory Structure

```text
.
├── calculator/            # Workspace directory for agent operations
│   ├── main.py
│   ├── tests.py
│   └── pkg/
│       ├── calculator.py
│       └── render.py
├── functions/             # Tool definitions and OpenAI function schemas
│   ├── get_file_content.py
│   ├── get_files_info.py
│   ├── run_python_file.py
│   └── write_file.py
├── call_function.py       # Tool execution mapper & dispatcher
├── config.py              # Configuration constants (e.g., MAX_CHARS)
├── main.py                # Main CLI entry point and agent loop
├── prompts.py             # System prompt definitions
├── pyproject.toml         # Dependency & project configuration
└── .env                   # Environment variables (API keys - gitignored)
```

Getting Started
Prerequisites:
Python 3.10+
uv (recommended) or pip
An OpenRouter API Key

Installation:
**Clone the repository:**
```
git clone [https://github.com/YOUR-USERNAME/AI-Agent-in-python.git](https://github.com/YOUR-USERNAME/AI-Agent-in-python.git)
cd AI-Agent-in-python
```
**Set up environment variables:**
Create a .env file in the root directory and add your OpenRouter API key:
```
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

Install dependencies:
**Using uv:**
```
uv sync
```
Usage:
Run the agent via main.py by providing a natural language task as a command-line argument:
```
uv run main.py "Explain how the calculator renders results to the console."
```
Verbose Mode:
Pass the --verbose flag to see prompt token counts, function execution details, and step-by-step tool outputs:
```
uv run main.py "Run the calculator tests and fix any failing test cases." --verbose
```
Testing:
Individual functions can be tested standalone using the dedicated test scripts in the root directory:
```
uv run test_get_files_info.py
uv run test_get_file_content.py
uv run test_write_file.py
uv run test_run_python_file.py
```
