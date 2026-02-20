"""CLI entry point for the Chaos Security Auditor.

Provides the ``csa`` command with sub-commands for each audit phase:

- ``csa recon``   — run contextual reconnaissance
- ``csa attack``  — generate and execute attack vectors
- ``csa report``  — produce the Chaos Report
"""

from __future__ import annotations

from pathlib import Path

import click

from chaos_auditor.config import AuditConfig, load_config


@click.group()
@click.version_option(package_name="chaos-security-auditor")
@click.option(
    "--config",
    "-c",
    type=click.Path(exists=True, path_type=Path),
    default=None,
    help="Path to YAML/TOML configuration file.",
)
@click.pass_context
def main(ctx: click.Context, config: Path | None) -> None:
    """Chaos Security Auditor — adversarial security testing in sandboxed environments."""
    ctx.ensure_object(dict)
    if config is not None:
        ctx.obj["config"] = load_config(config)
    else:
        ctx.obj["config"] = AuditConfig()


@main.command()
@click.option("--repo", "-r", required=True, help="Target repository URL or local path.")
@click.pass_context
def recon(ctx: click.Context, repo: str) -> None:
    """Phase 1: Contextual Reconnaissance — map tech stack, endpoints, and dependencies."""
    raise NotImplementedError("Recon phase not yet implemented.")


@main.command()
@click.option("--level", type=click.Choice(["app", "middleware", "infra", "all"]), default="all")
@click.pass_context
def attack(ctx: click.Context, level: str) -> None:
    """Phase 2-3: Generate attack vectors and execute the Hypothesize-Attack-Observe-Escalate loop."""
    raise NotImplementedError("Attack phase not yet implemented.")


@main.command()
@click.option("--output-format", type=click.Choice(["json", "markdown"]), default="markdown")
@click.option("--focus", multiple=True, help="Focus audit on specific components.")
@click.pass_context
def audit(ctx: click.Context, output_format: str, focus: tuple[str, ...]) -> None:
    """Run a full audit cycle (recon + attack + report)."""
    import json as _json
    import sys

    result = {"findings": [], "summary": "Audit completed (no attack vectors implemented yet)"}
    if output_format == "json":
        _json.dump(result, sys.stdout)
    else:
        click.echo("# Chaos Security Audit Report\n\nNo findings — attack vectors not yet implemented.")


@main.command()
@click.option("--output", "-o", type=click.Path(), default="reports/chaos_report.md")
@click.pass_context
def report(ctx: click.Context, output: str) -> None:
    """Generate the Chaos Report from collected findings."""
    raise NotImplementedError("Report generation not yet implemented.")


if __name__ == "__main__":
    main()
