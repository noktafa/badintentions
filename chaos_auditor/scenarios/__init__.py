"""Audit scenario catalogs.

Pre-built security audit scenarios organized by category, adapted from
real-world AI agent safety testing patterns. Each scenario defines
inputs, expected outcomes, and severity classifications.
"""

from chaos_auditor.scenarios.command_safety import (
    BLOCKED_COMMANDS,
    GRAYLIST_COMMANDS,
    SAFE_COMMANDS,
    CommandScenario,
    classify_command,
)
from chaos_auditor.scenarios.file_access import (
    READ_BLOCKED_PATHS,
    WRITE_BLOCKED_PATHS,
    FileAccessScenario,
    check_read_safety,
    check_write_safety,
)
from chaos_auditor.scenarios.secret_detection import (
    SECRET_PATTERNS,
    SecretScenario,
    redact_secrets,
)
from chaos_auditor.scenarios.interpreter_evasion import (
    EVASION_PATTERNS,
    SCRIPT_GRAYLIST,
    EvasionScenario,
    classify_interpreter_command,
)
from chaos_auditor.scenarios.content_scanning import (
    DANGEROUS_CONTENT,
    SAFE_CONTENT,
    ContentScenario,
    scan_write_content,
)
from chaos_auditor.scenarios.injection_defense import (
    wrap_tool_output,
    detect_write_then_execute,
)

__all__ = [
    "BLOCKED_COMMANDS",
    "CommandScenario",
    "ContentScenario",
    "DANGEROUS_CONTENT",
    "EVASION_PATTERNS",
    "EvasionScenario",
    "FileAccessScenario",
    "GRAYLIST_COMMANDS",
    "READ_BLOCKED_PATHS",
    "SAFE_COMMANDS",
    "SAFE_CONTENT",
    "SCRIPT_GRAYLIST",
    "SECRET_PATTERNS",
    "SecretScenario",
    "WRITE_BLOCKED_PATHS",
    "classify_command",
    "classify_interpreter_command",
    "check_read_safety",
    "check_write_safety",
    "detect_write_then_execute",
    "redact_secrets",
    "scan_write_content",
    "wrap_tool_output",
]
