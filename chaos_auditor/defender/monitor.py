"""Defender monitor — log watcher and response tracker.

Watches target and defender logs in real-time to:
- Detect whether the defender identified the attack.
- Measure time-to-detection (TTD) and time-to-response (TTR).
- Track automated countermeasures (IP blocks, WAF rules, alerts).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class DetectionEvent:
    """A single detection or response event from the defender."""

    timestamp: datetime
    source: str
    event_type: str  # "detection", "block", "alert", "mitigation"
    vector_id: str | None = None
    details: str = ""


@dataclass
class DefenderMetrics:
    """Aggregated defender performance metrics."""

    total_attacks: int = 0
    detected: int = 0
    blocked: int = 0
    mean_ttd_seconds: float = 0.0
    mean_ttr_seconds: float = 0.0
    events: list[DetectionEvent] = field(default_factory=list)

    @property
    def detection_rate(self) -> float:
        """Fraction of attacks detected by the defender."""
        if self.total_attacks == 0:
            return 0.0
        return self.detected / self.total_attacks


class DefenderMonitor:
    """Watches defender logs and tracks detection/response metrics.

    Parameters
    ----------
    log_source:
        Path or URL to the defender log stream.
    """

    def __init__(self, log_source: str) -> None:
        self.log_source = log_source
        self._metrics = DefenderMetrics()

    def start(self) -> None:
        """Begin watching the defender log stream."""
        raise NotImplementedError

    def stop(self) -> DefenderMetrics:
        """Stop watching and return aggregated metrics.

        Returns
        -------
        DefenderMetrics
            Detection and response performance metrics.
        """
        raise NotImplementedError

    def record_attack(self, vector_id: str, timestamp: datetime) -> None:
        """Notify the monitor that an attack was launched.

        Parameters
        ----------
        vector_id:
            The ID of the executed attack vector.
        timestamp:
            When the attack was launched.
        """
        raise NotImplementedError

    @property
    def metrics(self) -> DefenderMetrics:
        """Current defender metrics snapshot."""
        return self._metrics
