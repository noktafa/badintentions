"""Chaos Report generation.

Produces structured Markdown reports from execution records using
Jinja2 templates.
"""

from chaos_auditor.reporting.report import ChaosReport, Finding, generate_report

__all__ = [
    "ChaosReport",
    "Finding",
    "generate_report",
]
