"""Tests for secret detection and redaction scenarios."""

from __future__ import annotations

import re

import pytest

from chaos_auditor.scenarios.secret_detection import (
    COMPILED_PATTERNS,
    SECRET_PATTERNS,
    SecretScenario,
    redact_secrets,
)


class TestScenarioData:
    """Validate scenario data integrity."""

    def test_patterns_not_empty(self) -> None:
        assert len(SECRET_PATTERNS) >= 8

    def test_all_expected_redacted(self) -> None:
        for s in SECRET_PATTERNS:
            assert s.expected_redacted is True

    def test_all_have_providers(self) -> None:
        for s in SECRET_PATTERNS:
            assert s.provider, f"Missing provider for {s.description}"

    def test_compiled_patterns_count_matches(self) -> None:
        assert len(COMPILED_PATTERNS) == len(SECRET_PATTERNS)


class TestPatternMatching:
    """Verify each regex pattern matches its example input."""

    @pytest.mark.parametrize(
        "scenario",
        SECRET_PATTERNS,
        ids=[s.description for s in SECRET_PATTERNS],
    )
    def test_pattern_matches_input(self, scenario: SecretScenario) -> None:
        pattern = re.compile(scenario.pattern)
        match = pattern.search(scenario.input_text)
        assert match is not None, (
            f"Pattern {scenario.pattern!r} did not match "
            f"input {scenario.input_text!r}"
        )


class TestProviderCoverage:
    """Verify coverage across secret providers."""

    def test_covers_openai(self) -> None:
        providers = {s.provider for s in SECRET_PATTERNS}
        assert "openai" in providers

    def test_covers_aws(self) -> None:
        providers = {s.provider for s in SECRET_PATTERNS}
        assert "aws" in providers

    def test_covers_github(self) -> None:
        providers = {s.provider for s in SECRET_PATTERNS}
        assert "github" in providers

    def test_covers_gitlab(self) -> None:
        providers = {s.provider for s in SECRET_PATTERNS}
        assert "gitlab" in providers

    def test_covers_slack(self) -> None:
        providers = {s.provider for s in SECRET_PATTERNS}
        assert "slack" in providers

    def test_covers_generic(self) -> None:
        providers = {s.provider for s in SECRET_PATTERNS}
        assert "generic" in providers


class TestRedactSecrets:
    """Test the redact_secrets stub."""

    def test_not_implemented(self) -> None:
        with pytest.raises(NotImplementedError):
            redact_secrets("sk-abc123def456ghi789jkl012mno345")
