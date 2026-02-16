"""Tests for the configuration module."""

from __future__ import annotations

from pathlib import Path

import pytest

from chaos_auditor.config import AuditConfig, SandboxConfig, load_config


class TestSandboxConfig:
    """Tests for SandboxConfig validation."""

    def test_defaults(self) -> None:
        cfg = SandboxConfig()
        assert cfg.timeout_seconds == 300
        assert cfg.memory_limit == "512m"
        assert cfg.cpu_limit == 1.0

    def test_negative_timeout_raises(self) -> None:
        with pytest.raises(ValueError, match="timeout_seconds must be positive"):
            SandboxConfig(timeout_seconds=-1)

    def test_zero_timeout_raises(self) -> None:
        with pytest.raises(ValueError, match="timeout_seconds must be positive"):
            SandboxConfig(timeout_seconds=0)

    def test_negative_cpu_raises(self) -> None:
        with pytest.raises(ValueError, match="cpu_limit must be positive"):
            SandboxConfig(cpu_limit=-0.5)

    def test_invalid_memory_format_raises(self) -> None:
        with pytest.raises(ValueError, match="memory_limit must match"):
            SandboxConfig(memory_limit="abc")

    def test_valid_memory_formats(self) -> None:
        for fmt in ("512m", "1g", "256k", "1024M", "2G"):
            cfg = SandboxConfig(memory_limit=fmt)
            assert cfg.memory_limit == fmt


class TestAuditConfig:
    """Tests for AuditConfig validation."""

    def test_defaults(self) -> None:
        cfg = AuditConfig()
        assert cfg.phases == ["recon", "vectors", "execute"]
        assert cfg.vector_levels == ["app", "middleware", "infra"]

    def test_invalid_phase_raises(self) -> None:
        with pytest.raises(ValueError, match="Unknown phases"):
            AuditConfig(phases=["recon", "bogus"])

    def test_invalid_vector_level_raises(self) -> None:
        with pytest.raises(ValueError, match="Unknown vector levels"):
            AuditConfig(vector_levels=["app", "bogus"])


class TestLoadConfig:
    """Tests for config file loading."""

    def test_load_config_not_implemented(self, tmp_path: Path) -> None:
        with pytest.raises(NotImplementedError):
            load_config(tmp_path / "config.yaml")
