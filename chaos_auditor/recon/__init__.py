"""Phase 1 — Contextual Reconnaissance.

Modules in this package map the target's technology stack, attack surface,
and known dependency vulnerabilities before any active testing begins.
"""

from chaos_auditor.recon.dependency_audit import VulnerablePackage, audit_dependencies, scan_manifests
from chaos_auditor.recon.repo_mapper import RepoProfile, clone_repo, detect_stack
from chaos_auditor.recon.surface_analyzer import AttackSurface, Endpoint, map_attack_surface, map_endpoints

__all__ = [
    "AttackSurface",
    "Endpoint",
    "RepoProfile",
    "VulnerablePackage",
    "audit_dependencies",
    "clone_repo",
    "detect_stack",
    "map_attack_surface",
    "map_endpoints",
    "scan_manifests",
]
