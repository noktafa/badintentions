"""Configuration loader for the Chaos Security Auditor.

Supports YAML and TOML configuration files that define target scope,
attack parameters, sandbox settings, and reporting preferences.
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from chaos_auditor import VALID_PHASES, VALID_VECTOR_LEVELS

_MEMORY_RE = re.compile(r"^\d+[kmgKMG]?$")


@dataclass
class SandboxConfig:
    """Docker sandbox isolation settings."""

    network: str = "sandbox"
    timeout_seconds: int = 300
    memory_limit: str = "512m"
    cpu_limit: float = 1.0

    def __post_init__(self) -> None:
        if self.timeout_seconds <= 0:
            raise ValueError(f"timeout_seconds must be positive, got {self.timeout_seconds}")
        if self.cpu_limit <= 0:
            raise ValueError(f"cpu_limit must be positive, got {self.cpu_limit}")
        if not _MEMORY_RE.match(self.memory_limit):
            raise ValueError(
                f"memory_limit must match '<number>[k|m|g]', got {self.memory_limit!r}"
            )


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

    def __post_init__(self) -> None:
        invalid_phases = set(self.phases) - VALID_PHASES
        if invalid_phases:
            raise ValueError(f"Unknown phases: {invalid_phases}. Valid: {VALID_PHASES}")
        invalid_levels = set(self.vector_levels) - VALID_VECTOR_LEVELS
        if invalid_levels:
            raise ValueError(
                f"Unknown vector levels: {invalid_levels}. Valid: {VALID_VECTOR_LEVELS}"
            )


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
