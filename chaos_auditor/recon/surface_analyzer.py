"""Attack-surface analyser — map endpoints, webhooks, and database schemas.

Scans source code and configuration files to enumerate:
- HTTP/gRPC/WebSocket endpoints and their auth requirements.
- Webhook receivers and outbound integrations.
- Database schema definitions and migration files.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Endpoint:
    """A discovered API endpoint."""

    method: str
    path: str
    auth_required: bool = False
    parameters: list[str] = field(default_factory=list)


@dataclass
class AttackSurface:
    """Aggregated attack surface of the target."""

    endpoints: list[Endpoint] = field(default_factory=list)
    webhooks: list[str] = field(default_factory=list)
    db_schemas: list[str] = field(default_factory=list)


def map_endpoints(repo_root: Path) -> list[Endpoint]:
    """Extract API endpoints from source code and route definitions.

    Parameters
    ----------
    repo_root:
        Path to the target repository root.

    Returns
    -------
    list[Endpoint]
        Discovered endpoints with method, path, and auth metadata.
    """
    raise NotImplementedError


def map_attack_surface(repo_root: Path) -> AttackSurface:
    """Build a full :class:`AttackSurface` model for the target.

    Parameters
    ----------
    repo_root:
        Path to the target repository root.

    Returns
    -------
    AttackSurface
        Complete attack-surface mapping.
    """
    raise NotImplementedError
