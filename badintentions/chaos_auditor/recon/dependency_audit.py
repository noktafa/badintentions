"""Dependency auditor — scan package manifests for known CVEs.

Parses dependency files (``requirements.txt``, ``package.json``,
``go.mod``, etc.) and cross-references versions against vulnerability
databases (NVD, OSV, GitHub Advisories).
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class VulnerablePackage:
    """A dependency with at least one known vulnerability."""

    name: str
    installed_version: str
    cve_ids: list[str] = field(default_factory=list)
    severity: str = "unknown"
    fixed_version: str | None = None


def scan_manifests(repo_root: Path) -> list[Path]:
    """Locate all package manifest files in the repository.

    Parameters
    ----------
    repo_root:
        Path to the target repository root.

    Returns
    -------
    list[Path]
        Paths to detected manifest files.
    """
    raise NotImplementedError


def audit_dependencies(manifest: Path) -> list[VulnerablePackage]:
    """Check a single manifest for vulnerable dependencies.

    Parameters
    ----------
    manifest:
        Path to a package manifest file.

    Returns
    -------
    list[VulnerablePackage]
        Dependencies with known CVEs.
    """
    raise NotImplementedError
