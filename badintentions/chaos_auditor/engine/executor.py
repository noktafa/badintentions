"""Execution engine — Hypothesize → Attack → Observe → Escalate loop.

Drives the core audit cycle:

1. **Hypothesize** — select the next vector and predict the expected outcome.
2. **Attack** — execute the vector payload against the sandbox target.
3. **Observe** — capture responses, logs, and side-effects.
4. **Escalate** — if a weakness is confirmed, generate deeper follow-up vectors.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class StepResult(Enum):
    """Outcome of a single execution step."""

    SUCCESS = "success"
    FAILURE = "failure"
    ERROR = "error"
    SKIPPED = "skipped"


@dataclass
class ExecutionRecord:
    """Immutable record of a single attack execution."""

    vector_id: str
    hypothesis: str
    result: StepResult
    response: dict[str, Any] = field(default_factory=dict)
    observations: list[str] = field(default_factory=list)
    escalations: list[str] = field(default_factory=list)


class Executor:
    """Runs the Hypothesize → Attack → Observe → Escalate loop.

    Parameters
    ----------
    target_url:
        Base URL of the sandbox target service.
    timeout:
        Per-vector execution timeout in seconds.
    """

    def __init__(self, target_url: str, timeout: int = 30) -> None:
        self.target_url = target_url
        self.timeout = timeout
        self._history: list[ExecutionRecord] = []

    def hypothesize(self, vector_id: str) -> str:
        """Predict the expected outcome for a given vector.

        Parameters
        ----------
        vector_id:
            Identifier of the attack vector.

        Returns
        -------
        str
            A human-readable hypothesis statement.
        """
        raise NotImplementedError

    def attack(self, vector_id: str, payload: str) -> dict[str, Any]:
        """Execute an attack vector payload against the target.

        Parameters
        ----------
        vector_id:
            Identifier of the attack vector.
        payload:
            The attack payload string.

        Returns
        -------
        dict[str, Any]
            Raw response data from the target.
        """
        raise NotImplementedError

    def observe(self, vector_id: str, response: dict[str, Any]) -> list[str]:
        """Analyse the target response and collect observations.

        Parameters
        ----------
        vector_id:
            Identifier of the attack vector.
        response:
            Raw response from :meth:`attack`.

        Returns
        -------
        list[str]
            Observations and anomalies detected.
        """
        raise NotImplementedError

    def escalate(self, vector_id: str, observations: list[str]) -> list[str]:
        """Generate follow-up vectors based on confirmed weaknesses.

        Parameters
        ----------
        vector_id:
            Identifier of the original attack vector.
        observations:
            Observations from :meth:`observe`.

        Returns
        -------
        list[str]
            IDs of newly generated escalation vectors.
        """
        raise NotImplementedError

    def run(self, vector_id: str, payload: str) -> ExecutionRecord:
        """Execute the full H→A→O→E cycle for one vector.

        Parameters
        ----------
        vector_id:
            Identifier of the attack vector.
        payload:
            The attack payload string.

        Returns
        -------
        ExecutionRecord
            Complete record of the execution.
        """
        raise NotImplementedError

    @property
    def history(self) -> list[ExecutionRecord]:
        """Return the full execution history."""
        return list(self._history)
