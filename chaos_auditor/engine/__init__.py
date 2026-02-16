"""Phase 3 — Execution Loop.

Orchestrates the Hypothesize → Attack → Observe → Escalate cycle,
prioritising vectors by likelihood and impact.
"""

from chaos_auditor.engine.executor import ExecutionRecord, Executor, StepResult
from chaos_auditor.engine.scheduler import ScoredVector, compute_score, schedule

__all__ = [
    "ExecutionRecord",
    "Executor",
    "ScoredVector",
    "StepResult",
    "compute_score",
    "schedule",
]
