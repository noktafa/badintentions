"""Chaos Security Auditor — AI-driven adversarial security testing framework.

Combines chaos engineering with automated penetration testing inside
sandboxed environments.  The framework operates in three phases:

1. **Contextual Reconnaissance** — map the target's tech stack, endpoints,
   and dependencies.
2. **Attack Vector Generation** — produce application-, middleware-, and
   infrastructure-level attack scenarios.
3. **Execution Loop** — run Hypothesize → Attack → Observe → Escalate cycles
   and generate a Chaos Report.
"""

from __future__ import annotations

from enum import Enum

__version__ = "0.1.0"


class Severity(Enum):
    """CVSS-aligned severity rating used across all modules."""

    INFO = "info"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


VALID_PHASES = frozenset({"recon", "vectors", "execute"})
VALID_VECTOR_LEVELS = frozenset({"app", "middleware", "infra"})
