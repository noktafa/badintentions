"""Configuration loader for the Chaos Security Auditor.

Supports YAML and TOML configuration files that define target scope,
attack parameters, sandbox settings, and reporting preferences.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any


@dataclass
class SandboxConfig:
    """Docker sandbox isolation settings."""

    network: str = "sandbox"
    timeout_seconds: int = 300
    memory_limit: str = "512m"
    cpu_limit: float = 1.0


@dataclass
class AuditConfig:
    """Top-level audit configuration."""

    target_repo: str = ""
    target_url: str = ""
    phases: list[str] = field(default_factory=lambda: ["recon", "vectors", "execute"])
    vector_levels: list[str] = field(default_factory=lambda: ["app", "middleware", "infra"])
    sandbox: SandboxConfig = field(default_factory=SandboxConfig)
    report_output: str = "reports/chaos_report.md"
    extra: dict[str, Any] = field(default_factory=dict)


def load_config(path: Path) -> AuditConfig:
    """Load an :class:`AuditConfig` from a YAML or TOML file.

    Parameters
    ----------
    path:
        Filesystem path to the configuration file.  The format is
        determined by the file extension (``.yaml`` / ``.yml`` for YAML,
        ``.toml`` for TOML).

    Returns
    -------
    AuditConfig
        Parsed configuration dataclass.

    Raises
    ------
    NotImplementedError
        Always — implementation pending.
    """
    raise NotImplementedError(f"Config loading from {path} not yet implemented.")
