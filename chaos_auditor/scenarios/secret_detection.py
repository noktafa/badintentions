"""Secret detection and redaction scenarios.

Defines patterns for API keys, tokens, and credentials that must be
detected and redacted in logs, outputs, and reports. Patterns cover
major providers: OpenAI, AWS, GitHub, GitLab, Slack, and generic JWTs.
"""

from __future__ import annotations

import re
from dataclasses import dataclass


@dataclass(frozen=True)
class SecretScenario:
    """A secret detection test case."""

    input_text: str
    expected_redacted: bool
    description: str
    provider: str  # e.g., "openai", "aws", "github", "generic"
    pattern: str  # regex pattern that should match


SECRET_PATTERNS: list[SecretScenario] = [
    SecretScenario(
        input_text="sk-abc123def456ghi789jkl012mno345",
        expected_redacted=True,
        description="OpenAI API key (legacy format)",
        provider="openai",
        pattern=r"sk-[a-zA-Z0-9]{20,}",
    ),
    SecretScenario(
        input_text="sk-proj-abc123def456ghi789jkl012mno345pqr",
        expected_redacted=True,
        description="OpenAI API key (project format)",
        provider="openai",
        pattern=r"sk-proj-[a-zA-Z0-9]{20,}",
    ),
    SecretScenario(
        input_text="AKIAIOSFODNN7EXAMPLE",
        expected_redacted=True,
        description="AWS Access Key ID",
        provider="aws",
        pattern=r"AKIA[0-9A-Z]{16}",
    ),
    SecretScenario(
        input_text="ghp_ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijkl",
        expected_redacted=True,
        description="GitHub Personal Access Token",
        provider="github",
        pattern=r"ghp_[a-zA-Z0-9]{36,}",
    ),
    SecretScenario(
        input_text="glpat-ABCDEFGHIJKLMNOPQRSTUVWx",
        expected_redacted=True,
        description="GitLab Personal Access Token",
        provider="gitlab",
        pattern=r"glpat-[a-zA-Z0-9]{20,}",
    ),
    SecretScenario(
        input_text="xoxb-1234567890-abcdefghij",
        expected_redacted=True,
        description="Slack Bot Token",
        provider="slack",
        pattern=r"xox[baprs]-[a-zA-Z0-9\-]+",
    ),
    SecretScenario(
        input_text="Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6",
        expected_redacted=True,
        description="JWT Bearer Token",
        provider="generic",
        pattern=r"Bearer\s+eyJ[a-zA-Z0-9_\-]+",
    ),
    SecretScenario(
        input_text="export API_KEY=mysecretvalue123",
        expected_redacted=True,
        description="Environment variable export with secret",
        provider="generic",
        pattern=r"export\s+\w*(KEY|SECRET|TOKEN|PASSWORD)\w*=\S+",
    ),
]

# Pre-compiled regex patterns for runtime use
COMPILED_PATTERNS: list[re.Pattern[str]] = [
    re.compile(s.pattern) for s in SECRET_PATTERNS
]


def redact_secrets(text: str) -> str:
    """Replace detected secrets in text with ``[REDACTED]``.

    Parameters
    ----------
    text:
        Input text that may contain secrets.

    Returns
    -------
    str
        Text with all matched secrets replaced by ``[REDACTED]``.
    """
    raise NotImplementedError
