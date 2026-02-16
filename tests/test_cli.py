"""Tests for the CLI entry point."""

from __future__ import annotations

from click.testing import CliRunner

from chaos_auditor.cli import main


class TestCLI:
    """Tests for Click CLI commands."""

    def test_help(self) -> None:
        runner = CliRunner()
        result = runner.invoke(main, ["--help"])
        assert result.exit_code == 0
        assert "Chaos Security Auditor" in result.output

    def test_recon_help(self) -> None:
        runner = CliRunner()
        result = runner.invoke(main, ["recon", "--help"])
        assert result.exit_code == 0
        assert "--repo" in result.output

    def test_attack_help(self) -> None:
        runner = CliRunner()
        result = runner.invoke(main, ["attack", "--help"])
        assert result.exit_code == 0
        assert "--level" in result.output

    def test_report_help(self) -> None:
        runner = CliRunner()
        result = runner.invoke(main, ["report", "--help"])
        assert result.exit_code == 0
        assert "--output" in result.output

    def test_recon_requires_repo(self) -> None:
        runner = CliRunner()
        result = runner.invoke(main, ["recon"])
        assert result.exit_code != 0
        assert "Missing option" in result.output or "required" in result.output.lower()
