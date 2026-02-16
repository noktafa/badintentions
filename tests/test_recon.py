"""Tests for the recon phase (Phase 1)."""

from __future__ import annotations

import pytest

from chaos_auditor.recon.repo_mapper import RepoProfile, detect_stack
from chaos_auditor.recon.surface_analyzer import AttackSurface, map_attack_surface
from chaos_auditor.recon.dependency_audit import VulnerablePackage, audit_dependencies


class TestRepoMapper:
    """Tests for repo_mapper module."""

    def test_detect_stack_not_implemented(self, tmp_path: str) -> None:
        with pytest.raises(NotImplementedError):
            detect_stack(tmp_path)

    def test_repo_profile_defaults(self) -> None:
        from pathlib import Path

        profile = RepoProfile(path=Path("."))
        assert profile.languages == []
        assert profile.frameworks == []


class TestSurfaceAnalyzer:
    """Tests for surface_analyzer module."""

    def test_map_attack_surface_not_implemented(self) -> None:
        with pytest.raises(NotImplementedError):
            map_attack_surface("/tmp/repo")

    def test_attack_surface_defaults(self) -> None:
        surface = AttackSurface()
        assert surface.endpoints == []
        assert surface.webhooks == []


class TestDependencyAudit:
    """Tests for dependency_audit module."""

    def test_audit_dependencies_not_implemented(self, tmp_path: str) -> None:
        from pathlib import Path

        with pytest.raises(NotImplementedError):
            audit_dependencies(Path(tmp_path) / "requirements.txt")

    def test_vulnerable_package_defaults(self) -> None:
        pkg = VulnerablePackage(name="example", installed_version="1.0.0")
        assert pkg.severity == "unknown"
        assert pkg.fixed_version is None
