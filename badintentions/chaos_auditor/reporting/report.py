"""Report model and generator.

Collects execution records, enriches them with severity and remediation
metadata, and renders a Chaos Report via a Jinja2 markdown template.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class Finding:
    """A single security finding for the report."""

    vector_id: str
    title: str
    severity: str
    description: str
    evidence: str
    remediation: str
    references: list[str] = field(default_factory=list)


@dataclass
class ChaosReport:
    """Structured Chaos Report model."""

    target: str
    timestamp: str
    summary: str
    findings: list[Finding] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    @property
    def critical_count(self) -> int:
        """Number of critical-severity findings."""
        return sum(1 for f in self.findings if f.severity == "critical")

    @property
    def high_count(self) -> int:
        """Number of high-severity findings."""
        return sum(1 for f in self.findings if f.severity == "high")


def generate_report(report: ChaosReport, output: Path) -> Path:
    """Render a :class:`ChaosReport` to a Markdown file using Jinja2.

    Parameters
    ----------
    report:
        Populated report model.
    output:
        Destination file path.

    Returns
    -------
    Path
        The path to the written report file.
    """
    raise NotImplementedError
