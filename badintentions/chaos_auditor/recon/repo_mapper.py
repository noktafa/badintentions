"""Repository mapper — clone targets and detect their technology stack.

Responsible for:
- Cloning or referencing a local/remote repository.
- Identifying languages, frameworks, and build systems.
- Producing a :class:`RepoProfile` consumed by downstream phases.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class RepoProfile:
    """Summarises the technology stack of a scanned repository."""

    path: Path
    languages: list[str] = field(default_factory=list)
    frameworks: list[str] = field(default_factory=list)
    build_systems: list[str] = field(default_factory=list)
    package_files: list[Path] = field(default_factory=list)


def clone_repo(url: str, dest: Path) -> Path:
    """Clone a remote repository to *dest*.

    Parameters
    ----------
    url:
        Git-compatible remote URL.
    dest:
        Local directory to clone into.

    Returns
    -------
    Path
        The root of the cloned repository.
    """
    raise NotImplementedError


def detect_stack(repo_root: Path) -> RepoProfile:
    """Analyse a repository and return its :class:`RepoProfile`.

    Parameters
    ----------
    repo_root:
        Path to the root of the target repository.

    Returns
    -------
    RepoProfile
        Detected technology stack metadata.
    """
    raise NotImplementedError
