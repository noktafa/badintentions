"""Tests for the defender monitoring module."""

from __future__ import annotations

from datetime import datetime

import pytest

from chaos_auditor.defender.monitor import DefenderMetrics, DefenderMonitor, DetectionEvent


class TestDetectionEvent:
    """Tests for DetectionEvent dataclass."""

    def test_defaults(self) -> None:
        event = DetectionEvent(
            timestamp=datetime(2025, 1, 1),
            source="waf",
            event_type="detection",
        )
        assert event.vector_id is None
        assert event.details == ""


class TestDefenderMetrics:
    """Tests for DefenderMetrics dataclass."""

    def test_detection_rate_zero_attacks(self) -> None:
        metrics = DefenderMetrics()
        assert metrics.detection_rate == 0.0

    def test_detection_rate_calculation(self) -> None:
        metrics = DefenderMetrics(total_attacks=10, detected=7)
        assert metrics.detection_rate == pytest.approx(0.7)

    def test_defaults(self) -> None:
        metrics = DefenderMetrics()
        assert metrics.total_attacks == 0
        assert metrics.events == []


class TestDefenderMonitor:
    """Tests for DefenderMonitor class."""

    def test_init(self) -> None:
        monitor = DefenderMonitor(log_source="/var/log/defender.log")
        assert monitor.log_source == "/var/log/defender.log"
        assert monitor.metrics.total_attacks == 0

    def test_start_not_implemented(self) -> None:
        monitor = DefenderMonitor(log_source="test")
        with pytest.raises(NotImplementedError):
            monitor.start()

    def test_stop_not_implemented(self) -> None:
        monitor = DefenderMonitor(log_source="test")
        with pytest.raises(NotImplementedError):
            monitor.stop()

    def test_record_attack_not_implemented(self) -> None:
        monitor = DefenderMonitor(log_source="test")
        with pytest.raises(NotImplementedError):
            monitor.record_attack("v1", datetime(2025, 1, 1))
