"""Phase 2 — Attack Vector Generation.

Modules in this package produce attack vectors at three levels:
- **Application** — BOLA, injection, business-logic flaws.
- **Middleware** — Broker, cache, and storage misconfigurations.
- **Infrastructure** — Container escapes, Dockerfile flaws, resource exhaustion.
"""

from chaos_auditor.vectors.application import (
    AttackVector,
    generate_bola_vectors,
    generate_injection_vectors,
    generate_logic_flaw_vectors,
)
from chaos_auditor.vectors.infrastructure import (
    generate_container_escape_vectors,
    generate_dockerfile_vectors,
    generate_resource_exhaustion_vectors,
)
from chaos_auditor.vectors.middleware import (
    MiddlewareTarget,
    generate_broker_vectors,
    generate_cache_vectors,
    generate_storage_vectors,
)

__all__ = [
    "AttackVector",
    "MiddlewareTarget",
    "generate_bola_vectors",
    "generate_broker_vectors",
    "generate_cache_vectors",
    "generate_container_escape_vectors",
    "generate_dockerfile_vectors",
    "generate_injection_vectors",
    "generate_logic_flaw_vectors",
    "generate_resource_exhaustion_vectors",
    "generate_storage_vectors",
]
