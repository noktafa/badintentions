"""Interpreter evasion and script execution scenarios.

Detects attempts to bypass command-level safety checks via:
- Inline interpreter execution (python3 -c, perl -e, node -e, etc.)
- eval / bash -c / sh -c indirection
- Base64-encoded payload execution
- PowerShell Invoke-Expression
- Dangerous crontab and find operations
- Script file execution requiring confirmation
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class EvasionScenario:
    """An interpreter evasion test case."""

    command: str
    expected: str  # "blocked", "confirm", or "safe"
    description: str
    technique: str  # e.g., "inline_interpreter", "eval", "base64", "powershell"


# --- Evasion patterns: must be BLOCKED ---

EVASION_PATTERNS: list[EvasionScenario] = [
    # Inline interpreter execution
    EvasionScenario(
        command='python3 -c "import os"',
        expected="blocked",
        description="Python inline code execution",
        technique="inline_interpreter",
    ),
    EvasionScenario(
        command='perl -e "system(1)"',
        expected="blocked",
        description="Perl inline code execution",
        technique="inline_interpreter",
    ),
    EvasionScenario(
        command='ruby -e "puts 1"',
        expected="blocked",
        description="Ruby inline code execution",
        technique="inline_interpreter",
    ),
    EvasionScenario(
        command='node -e "console.log(1)"',
        expected="blocked",
        description="Node.js inline code execution",
        technique="inline_interpreter",
    ),
    # eval / shell indirection
    EvasionScenario(
        command='eval "echo pwned"',
        expected="blocked",
        description="eval with double-quoted string",
        technique="eval",
    ),
    EvasionScenario(
        command="eval 'echo pwned'",
        expected="blocked",
        description="eval with single-quoted string",
        technique="eval",
    ),
    EvasionScenario(
        command='bash -c "whoami"',
        expected="blocked",
        description="bash -c inline execution",
        technique="shell_indirection",
    ),
    EvasionScenario(
        command='sh -c "id"',
        expected="blocked",
        description="sh -c inline execution",
        technique="shell_indirection",
    ),
    # Base64 encoded payloads
    EvasionScenario(
        command="echo dG90bw== | base64 -d | bash",
        expected="blocked",
        description="Base64-encoded payload piped to bash",
        technique="base64",
    ),
    EvasionScenario(
        command="base64 -d payload.txt | sh",
        expected="blocked",
        description="Base64 file decode piped to sh",
        technique="base64",
    ),
    # PowerShell
    EvasionScenario(
        command="Invoke-Expression 'Get-Process'",
        expected="blocked",
        description="PowerShell Invoke-Expression",
        technique="powershell",
    ),
    EvasionScenario(
        command="iex(something)",
        expected="blocked",
        description="PowerShell iex shorthand",
        technique="powershell",
    ),
    # Dangerous crontab/find operations
    EvasionScenario(
        command="crontab -r",
        expected="blocked",
        description="Crontab removal",
        technique="crontab",
    ),
    EvasionScenario(
        command="crontab -e",
        expected="blocked",
        description="Crontab editing",
        technique="crontab",
    ),
    EvasionScenario(
        command="find /tmp -name '*.log' | xargs rm",
        expected="blocked",
        description="xargs rm (bulk delete via pipe)",
        technique="find_delete",
    ),
    EvasionScenario(
        command="find / -name '*.bak' -exec rm {} ;",
        expected="blocked",
        description="find -exec rm (bulk delete)",
        technique="find_delete",
    ),
    EvasionScenario(
        command="find /tmp -delete",
        expected="blocked",
        description="find -delete (bulk delete)",
        technique="find_delete",
    ),
]


# --- Script execution graylist: require CONFIRM ---

SCRIPT_GRAYLIST: list[EvasionScenario] = [
    EvasionScenario(
        command="bash deploy.sh",
        expected="confirm",
        description="Bash script execution",
        technique="script_execution",
    ),
    EvasionScenario(
        command="sh setup.sh",
        expected="confirm",
        description="Shell script execution",
        technique="script_execution",
    ),
    EvasionScenario(
        command="python3 migrate.py",
        expected="confirm",
        description="Python script execution",
        technique="script_execution",
    ),
    EvasionScenario(
        command="perl transform.pl",
        expected="confirm",
        description="Perl script execution",
        technique="script_execution",
    ),
    EvasionScenario(
        command="ruby deploy.rb",
        expected="confirm",
        description="Ruby script execution",
        technique="script_execution",
    ),
    EvasionScenario(
        command="node server.js",
        expected="confirm",
        description="Node.js script execution",
        technique="script_execution",
    ),
    EvasionScenario(
        command="source ~/.bashrc",
        expected="confirm",
        description="Sourcing a shell config file",
        technique="script_execution",
    ),
]

# --- Safe command regression: must remain SAFE ---

SAFE_REGRESSION: list[EvasionScenario] = [
    EvasionScenario(
        command="ls -la",
        expected="safe",
        description="Directory listing still safe",
        technique="regression",
    ),
    EvasionScenario(
        command="cat /etc/hostname",
        expected="safe",
        description="Reading hostname still safe",
        technique="regression",
    ),
    EvasionScenario(
        command="python3 --version",
        expected="safe",
        description="Version check (not confused with python3 -c)",
        technique="regression",
    ),
    EvasionScenario(
        command="node --version",
        expected="safe",
        description="Version check (not confused with node -e)",
        technique="regression",
    ),
    EvasionScenario(
        command="crontab -l",
        expected="safe",
        description="Listing crontab (not confused with crontab -r/-e)",
        technique="regression",
    ),
    EvasionScenario(
        command="df -h",
        expected="safe",
        description="Disk usage still safe",
        technique="regression",
    ),
    EvasionScenario(
        command="ps aux",
        expected="safe",
        description="Process listing still safe",
        technique="regression",
    ),
    EvasionScenario(
        command="whoami",
        expected="safe",
        description="User identity still safe",
        technique="regression",
    ),
    EvasionScenario(
        command="uname -a",
        expected="safe",
        description="System info still safe",
        technique="regression",
    ),
]


def classify_interpreter_command(command: str) -> tuple[str, str | None]:
    """Classify a command for interpreter evasion attempts.

    Parameters
    ----------
    command:
        The shell command string to classify.

    Returns
    -------
    tuple[str, str | None]
        (classification, reason) — ``"blocked"``, ``"confirm"``, or ``"safe"``.
    """
    raise NotImplementedError
