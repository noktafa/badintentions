"""Tests for the reporting module."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

import pytest

from chaos_auditor import Severity
from chaos_auditor.reporting.report import ChaosReport, Finding, generate_report


class TestFinding:
    """Tests for the Finding dataclass."""

    def test_finding_with_severity_enum(self) -> None:
        f = Finding(
            vector_id="v1",
            title="Test",
            severity=Severity.CRITICAL,
            description="desc",
            evidence="ev",
            remediation="fix",
        )
        assert f.severity is Severity.CRITICAL
        assert f.references == []


class TestChaosReport:
    """Tests for the ChaosReport dataclass."""

    def test_empty_report_counts(self) -> None:
        report = ChaosReport(
            target="test",
            timestamp=datetime(2025, 1, 1),
            summary="empty",
        )
        assert report.critical_count == 0
        assert report.high_count == 0

    def test_severity_counting(self) -> None:
        findings = [
            Finding("v1", "A", Severity.CRITICAL, "d", "e", "r"),
            Finding("v2", "B", Severity.HIGH, "d", "e", "r"),
            Finding("v3", "C", Severity.CRITICAL, "d", "e", "r"),
            Finding("v4", "D", Severity.LOW, "d", "e", "r"),
        ]
        report = ChaosReport(
            target="test",
            timestamp=datetime(2025, 1, 1),
            summary="test",
            findings=findings,
        )
        assert report.critical_count == 2
        assert report.high_count == 1

    def test_timestamp_iso(self) -> None:
        report = ChaosReport(
            target="test",
            timestamp=datetime(2025, 6, 15, 12, 30, 0),
            summary="test",
        )
        assert report.timestamp_iso == "2025-06-15T12:30:00"

    def test_generate_report_not_implemented(self, tmp_path: Path) -> None:
        report = ChaosReport(
            target="test",
            timestamp=datetime(2025, 1, 1),
            summary="test",
        )
        with pytest.raises(NotImplementedError):
            generate_report(report, tmp_path / "out.md")
