"""Tests for write content scanning scenarios."""

from __future__ import annotations

import pytest

from chaos_auditor.scenarios.content_scanning import (
    DANGEROUS_CONTENT,
    SAFE_CONTENT,
    ContentScenario,
    scan_write_content,
)


class TestScenarioData:
    """Validate scenario data integrity."""

    def test_dangerous_content_not_empty(self) -> None:
        assert len(DANGEROUS_CONTENT) >= 9

    def test_safe_content_not_empty(self) -> None:
        assert len(SAFE_CONTENT) >= 3

    def test_all_dangerous_blocked(self) -> None:
        for s in DANGEROUS_CONTENT:
            assert s.expected == "blocked", f"{s.description} should be blocked"

    def test_all_safe_allowed(self) -> None:
        for s in SAFE_CONTENT:
            assert s.expected == "safe", f"{s.description} should be safe"

    def test_no_overlap(self) -> None:
        dangerous_set = {s.content for s in DANGEROUS_CONTENT}
        safe_set = {s.content for s in SAFE_CONTENT}
        assert not dangerous_set & safe_set, "Overlap between dangerous and safe content"


class TestDangerousContent:
    """Verify dangerous content scenarios cover key attack patterns."""

    @pytest.mark.parametrize(
        "scenario",
        DANGEROUS_CONTENT,
        ids=[s.description for s in DANGEROUS_CONTENT],
    )
    def test_dangerous_scenario(self, scenario: ContentScenario) -> None:
        assert scenario.expected == "blocked"
        assert scenario.content.strip()

    def test_covers_reverse_shell(self) -> None:
        cats = {s.category for s in DANGEROUS_CONTENT}
        assert "reverse_shell" in cats

    def test_covers_remote_code_execution(self) -> None:
        cats = {s.category for s in DANGEROUS_CONTENT}
        assert "remote_code_execution" in cats

    def test_covers_credential_access(self) -> None:
        cats = {s.category for s in DANGEROUS_CONTENT}
        assert "credential_access" in cats

    def test_covers_exfiltration(self) -> None:
        cats = {s.category for s in DANGEROUS_CONTENT}
        assert "exfiltration" in cats

    def test_covers_privilege_escalation(self) -> None:
        cats = {s.category for s in DANGEROUS_CONTENT}
        assert "privilege_escalation" in cats


class TestSafeContent:
    """Verify safe content is not falsely flagged."""

    @pytest.mark.parametrize(
        "scenario",
        SAFE_CONTENT,
        ids=[s.description for s in SAFE_CONTENT],
    )
    def test_safe_scenario(self, scenario: ContentScenario) -> None:
        assert scenario.expected == "safe"


class TestScanWriteContent:
    """Test the scan_write_content stub."""

    def test_not_implemented(self) -> None:
        with pytest.raises(NotImplementedError):
            scan_write_content("echo Hello")
