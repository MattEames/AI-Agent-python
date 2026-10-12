import os
import subprocess


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_path = os.path.normpath(os.path.join(working_dir_abs, file_path))

        # Check if file_path is within working_directory
        valid_target = (
            os.path.commonpath([working_dir_abs, target_path]) == working_dir_abs
        )
        if not valid_target:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        # Check if file exists and is a regular file
        if not os.path.isfile(target_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        # Check if file extension is .py
        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        # Build command list
        command = ["python3", target_path]
        if args:
            command.extend(args)

        # Execute process safely with timeout
        result = subprocess.run(
            command,
            cwd=working_dir_abs,
            capture_output=True,
            text=True,
            timeout=30,
        )

        # Build output string
        output_parts = []
        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")

        if not result.stdout and not result.stderr:
            output_parts.append("No output produced")
        else:
            if result.stdout:
                output_parts.append(f"STDOUT:\n{result.stdout.strip()}")
            if result.stderr:
                output_parts.append(f"STDERR:\n{result.stderr.strip()}")

        return "\n".join(output_parts)

    except Exception as e:
        return f"Error: executing Python file: {e}"

schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Executes a Python script file relative to the working directory with optional command-line arguments.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the Python file to execute, relative to the working directory.",
                },
                "args": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Optional command-line arguments to pass to the script.",
                },
            },
            "required": ["file_path"],
        },
    },
}
