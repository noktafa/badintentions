"""Vector scheduler — prioritisation and sequencing.

Orders attack vectors by a composite score of:
- **Severity** — CVSS-aligned rating.
- **Likelihood** — estimated probability of exploitation.
- **Blast radius** — potential impact scope.
- **Dependencies** — vectors that unlock follow-up attacks run first.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ScoredVector:
    """A vector annotated with scheduling metadata."""

    vector_id: str
    severity_score: float
    likelihood: float
    blast_radius: float
    composite_score: float = 0.0
    depends_on: list[str] = field(default_factory=list)


def compute_score(severity: float, likelihood: float, blast_radius: float) -> float:
    """Compute a composite priority score.

    Parameters
    ----------
    severity:
        Severity score (0.0–10.0).
    likelihood:
        Exploitation likelihood (0.0–1.0).
    blast_radius:
        Impact scope (0.0–1.0).

    Returns
    -------
    float
        Composite priority score.
    """
    raise NotImplementedError


def schedule(vectors: list[ScoredVector]) -> list[ScoredVector]:
    """Sort vectors into optimal execution order.

    Respects dependency ordering and maximises expected value
    of the audit by running high-composite-score vectors first.

    Parameters
    ----------
    vectors:
        Unordered list of scored vectors.

    Returns
    -------
    list[ScoredVector]
        Vectors sorted in recommended execution order.
    """
    raise NotImplementedError
