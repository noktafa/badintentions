"""Middleware-level attack vector generation.

Generates vectors targeting middleware components:

- **Message brokers** — Kafka/RabbitMQ ACL bypass, payload injection.
- **Cache stores** — Redis/Memcached unauthorized access, cache poisoning.
- **Object storage** — S3/GCS bucket misconfiguration, SSRF via signed URLs.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class MiddlewareTarget:
    """A discovered middleware component."""

    kind: str  # e.g., "redis", "kafka", "s3"
    host: str
    port: int
    authenticated: bool = False
    metadata: dict[str, str] = field(default_factory=dict)


def generate_broker_vectors(targets: list[MiddlewareTarget]) -> list[dict[str, str]]:
    """Generate attack vectors for message brokers.

    Parameters
    ----------
    targets:
        Discovered broker instances.

    Returns
    -------
    list[dict[str, str]]
        Broker-specific attack vectors.
    """
    raise NotImplementedError


def generate_cache_vectors(targets: list[MiddlewareTarget]) -> list[dict[str, str]]:
    """Generate attack vectors for cache stores (Redis, Memcached).

    Parameters
    ----------
    targets:
        Discovered cache instances.

    Returns
    -------
    list[dict[str, str]]
        Cache-specific attack vectors.
    """
    raise NotImplementedError


def generate_storage_vectors(targets: list[MiddlewareTarget]) -> list[dict[str, str]]:
    """Generate attack vectors for object storage (S3, GCS).

    Parameters
    ----------
    targets:
        Discovered storage instances.

    Returns
    -------
    list[dict[str, str]]
        Storage-specific attack vectors.
    """
    raise NotImplementedError
