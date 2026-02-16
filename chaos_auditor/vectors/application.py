"""Application-level attack vector generation.

Generates vectors targeting the application layer:

- **BOLA / IDOR** — Broken Object Level Authorization (OWASP API1).
- **Injection** — SQL, NoSQL, command, and template injection (CWE-89, CWE-78).
- **Business-logic flaws** — Race conditions, state-machine abuse, privilege escalation.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum


class Severity(Enum):
    """CVSS-aligned severity rating."""

    INFO = "info"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


@dataclass
class AttackVector:
    """A single attack vector with metadata."""

    id: str
    name: str
    category: str
    description: str
    severity: Severity = Severity.MEDIUM
    references: list[str] = field(default_factory=list)
    payload: str | None = None


def generate_bola_vectors(endpoints: list[dict[str, str]]) -> list[AttackVector]:
    """Generate Broken Object Level Authorization test vectors.

    Parameters
    ----------
    endpoints:
        Endpoint metadata from the recon phase.

    Returns
    -------
    list[AttackVector]
        BOLA/IDOR attack vectors targeting identified endpoints.
    """
    raise NotImplementedError


def generate_injection_vectors(endpoints: list[dict[str, str]]) -> list[AttackVector]:
    """Generate injection attack vectors (SQL, NoSQL, command, template).

    Parameters
    ----------
    endpoints:
        Endpoint metadata from the recon phase.

    Returns
    -------
    list[AttackVector]
        Injection vectors with payloads.
    """
    raise NotImplementedError


def generate_logic_flaw_vectors(endpoints: list[dict[str, str]]) -> list[AttackVector]:
    """Generate business-logic flaw vectors (race conditions, state abuse).

    Parameters
    ----------
    endpoints:
        Endpoint metadata from the recon phase.

    Returns
    -------
    list[AttackVector]
        Logic-flaw attack vectors.
    """
    raise NotImplementedError
