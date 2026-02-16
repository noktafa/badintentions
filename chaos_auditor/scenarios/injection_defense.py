"""Prompt injection defense and write-then-execute detection.

Provides two defense mechanisms for AI agent security:

1. **Output wrapping** — wraps tool output in delimiters to prevent
   LLM prompt injection via crafted command output.
2. **Write-then-execute detection** — flags attempts where an agent
   writes a script file and immediately executes it (supply-chain
   attack pattern).
"""

from __future__ import annotations


def wrap_tool_output(tool_name: str, output: str) -> str:
    """Wrap tool output in delimiters to prevent prompt injection.

    Encloses the output in ``[BEGIN <tool_name> OUTPUT]`` and
    ``[END <tool_name> OUTPUT]`` tags so the LLM can distinguish
    between tool results and injected instructions.

    Parameters
    ----------
    tool_name:
        Name of the tool that produced the output (e.g.,
        ``"run_shell_command"``).
    output:
        Raw output string from the tool.

    Returns
    -------
    str
        Delimited output string.
    """
    raise NotImplementedError


def detect_write_then_execute(
    command: str,
    recently_written: set[str],
) -> tuple[str, str | None]:
    """Detect if a command executes a recently-written script.

    Flags the supply-chain attack pattern where an agent writes a
    script file and then immediately executes it.

    Parameters
    ----------
    command:
        The shell command to check.
    recently_written:
        Set of file paths recently written by the agent.

    Returns
    -------
    tuple[str, str | None]
        ``("confirm", reason)`` if the command targets a recently
        written file, ``("safe", None)`` otherwise.
    """
    raise NotImplementedError


def extract_script_path(command: str) -> str | None:
    """Extract the script file path from a shell command.

    Parameters
    ----------
    command:
        Shell command string (e.g., ``"bash /tmp/deploy.sh"``).

    Returns
    -------
    str | None
        The script path if one is found, ``None`` otherwise.
    """
    raise NotImplementedError
