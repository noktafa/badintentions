"""Tests for command safety classification scenarios."""

from __future__ import annotations

import pytest

from chaos_auditor.scenarios.command_safety import (
    BLOCKED_COMMANDS,
    GRAYLIST_COMMANDS,
    SAFE_COMMANDS,
    CommandScenario,
    classify_command,
)


class TestScenarioData:
    """Validate scenario data integrity."""

    def test_blocked_commands_not_empty(self) -> None:
        assert len(BLOCKED_COMMANDS) >= 10

    def test_graylist_commands_not_empty(self) -> None:
        assert len(GRAYLIST_COMMANDS) >= 8

    def test_safe_commands_not_empty(self) -> None:
        assert len(SAFE_COMMANDS) >= 6

    def test_all_blocked_have_expected_blocked(self) -> None:
        for scenario in BLOCKED_COMMANDS:
            assert scenario.expected == "blocked", f"{scenario.command} should be blocked"

    def test_all_graylist_have_expected_confirm(self) -> None:
        for scenario in GRAYLIST_COMMANDS:
            assert scenario.expected == "confirm", f"{scenario.command} should be confirm"

    def test_all_safe_have_expected_safe(self) -> None:
        for scenario in SAFE_COMMANDS:
            assert scenario.expected == "safe", f"{scenario.command} should be safe"

    def test_no_duplicate_commands(self) -> None:
        all_cmds = [s.command for s in BLOCKED_COMMANDS + GRAYLIST_COMMANDS + SAFE_COMMANDS]
        assert len(all_cmds) == len(set(all_cmds)), "Duplicate command found"

    def test_all_have_descriptions(self) -> None:
        for scenario in BLOCKED_COMMANDS + GRAYLIST_COMMANDS + SAFE_COMMANDS:
            assert scenario.description, f"Missing description for {scenario.command}"

    def test_all_have_categories(self) -> None:
        for scenario in BLOCKED_COMMANDS + GRAYLIST_COMMANDS + SAFE_COMMANDS:
            assert scenario.category, f"Missing category for {scenario.command}"


class TestBlockedCommands:
    """Verify blocked command scenarios cover key attack patterns."""

    @pytest.mark.parametrize(
        "scenario",
        BLOCKED_COMMANDS,
        ids=[s.description for s in BLOCKED_COMMANDS],
    )
    def test_blocked_scenario(self, scenario: CommandScenario) -> None:
        assert scenario.expected == "blocked"
        assert scenario.command.strip()

    def test_covers_destructive(self) -> None:
        cats = {s.category for s in BLOCKED_COMMANDS}
        assert "destructive" in cats

    def test_covers_reverse_shell(self) -> None:
        cats = {s.category for s in BLOCKED_COMMANDS}
        assert "reverse_shell" in cats

    def test_covers_privilege_escalation(self) -> None:
        cats = {s.category for s in BLOCKED_COMMANDS}
        assert "privilege_escalation" in cats

    def test_covers_credential_access(self) -> None:
        cats = {s.category for s in BLOCKED_COMMANDS}
        assert "credential_access" in cats


class TestGraylistCommands:
    """Verify graylist command scenarios cover risky operations."""

    @pytest.mark.parametrize(
        "scenario",
        GRAYLIST_COMMANDS,
        ids=[s.description for s in GRAYLIST_COMMANDS],
    )
    def test_graylist_scenario(self, scenario: CommandScenario) -> None:
        assert scenario.expected == "confirm"
        assert scenario.command.strip()

    def test_covers_service_management(self) -> None:
        cats = {s.category for s in GRAYLIST_COMMANDS}
        assert "service_management" in cats

    def test_covers_network_security(self) -> None:
        cats = {s.category for s in GRAYLIST_COMMANDS}
        assert "network_security" in cats


class TestSafeCommands:
    """Verify safe command scenarios are purely read-only."""

    @pytest.mark.parametrize(
        "scenario",
        SAFE_COMMANDS,
        ids=[s.description for s in SAFE_COMMANDS],
    )
    def test_safe_scenario(self, scenario: CommandScenario) -> None:
        assert scenario.expected == "safe"
        assert scenario.command.strip()


class TestClassifyCommand:
    """Test the classify_command stub."""

    def test_not_implemented(self) -> None:
        with pytest.raises(NotImplementedError):
            classify_command("ls -la")
