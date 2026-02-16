"""Tests for the execution engine (Phase 3)."""

from __future__ import annotations

import pytest

from chaos_auditor.engine.executor import ExecutionRecord, Executor, StepResult
from chaos_auditor.engine.scheduler import ScoredVector, compute_score, schedule


class TestExecutor:
    """Tests for the execution engine."""

    def test_executor_init(self) -> None:
        ex = Executor(target_url="http://localhost:8080", timeout=60)
        assert ex.target_url == "http://localhost:8080"
        assert ex.timeout == 60
        assert ex.history == []

    def test_hypothesize_not_implemented(self) -> None:
        ex = Executor(target_url="http://localhost:8080")
        with pytest.raises(NotImplementedError):
            ex.hypothesize("v1")

    def test_attack_not_implemented(self) -> None:
        ex = Executor(target_url="http://localhost:8080")
        with pytest.raises(NotImplementedError):
            ex.attack("v1", "payload")

    def test_run_not_implemented(self) -> None:
        ex = Executor(target_url="http://localhost:8080")
        with pytest.raises(NotImplementedError):
            ex.run("v1", "payload")

    def test_execution_record_defaults(self) -> None:
        rec = ExecutionRecord(vector_id="v1", hypothesis="test", result=StepResult.SUCCESS)
        assert rec.observations == []
        assert rec.escalations == []


class TestScheduler:
    """Tests for vector scheduling."""

    def test_compute_score_not_implemented(self) -> None:
        with pytest.raises(NotImplementedError):
            compute_score(severity=9.0, likelihood=0.8, blast_radius=0.5)

    def test_schedule_not_implemented(self) -> None:
        with pytest.raises(NotImplementedError):
            schedule([])

    def test_scored_vector_defaults(self) -> None:
        sv = ScoredVector(
            vector_id="v1", severity_score=8.0, likelihood=0.9, blast_radius=0.7
        )
        assert sv.composite_score == 0.0
        assert sv.depends_on == []
