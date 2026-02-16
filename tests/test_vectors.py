"""Tests for the attack vector generation phase (Phase 2)."""

from __future__ import annotations

from pathlib import Path

import pytest

from chaos_auditor import Severity
from chaos_auditor.vectors.application import (
    AttackVector,
    generate_bola_vectors,
    generate_injection_vectors,
    generate_logic_flaw_vectors,
)
from chaos_auditor.vectors.middleware import MiddlewareTarget, generate_broker_vectors
from chaos_auditor.vectors.infrastructure import (
    generate_container_escape_vectors,
    generate_dockerfile_vectors,
    generate_resource_exhaustion_vectors,
)


class TestApplicationVectors:
    """Tests for application-level vector generation."""

    def test_generate_bola_not_implemented(self) -> None:
        with pytest.raises(NotImplementedError):
            generate_bola_vectors([])

    def test_generate_injection_not_implemented(self) -> None:
        with pytest.raises(NotImplementedError):
            generate_injection_vectors([])

    def test_generate_logic_flaw_not_implemented(self) -> None:
        with pytest.raises(NotImplementedError):
            generate_logic_flaw_vectors([])

    def test_attack_vector_defaults(self) -> None:
        vec = AttackVector(id="v1", name="test", category="test", description="test")
        assert vec.severity is Severity.MEDIUM
        assert vec.references == []


class TestMiddlewareVectors:
    """Tests for middleware-level vector generation."""

    def test_generate_broker_not_implemented(self) -> None:
        with pytest.raises(NotImplementedError):
            generate_broker_vectors([])

    def test_middleware_target_defaults(self) -> None:
        target = MiddlewareTarget(kind="redis", host="localhost", port=6379)
        assert target.authenticated is False


class TestInfrastructureVectors:
    """Tests for infrastructure-level vector generation."""

    def test_generate_container_escape_not_implemented(self, tmp_path: Path) -> None:
        with pytest.raises(NotImplementedError):
            generate_container_escape_vectors(tmp_path / "Dockerfile")

    def test_generate_dockerfile_not_implemented(self, tmp_path: Path) -> None:
        with pytest.raises(NotImplementedError):
            generate_dockerfile_vectors(tmp_path / "Dockerfile")

    def test_generate_resource_exhaustion_not_implemented(self) -> None:
        with pytest.raises(NotImplementedError):
            generate_resource_exhaustion_vectors()
