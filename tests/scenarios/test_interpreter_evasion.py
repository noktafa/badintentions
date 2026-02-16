"""Tests for interpreter evasion and script execution scenarios."""

from __future__ import annotations

import pytest

from chaos_auditor.scenarios.interpreter_evasion import (
    EVASION_PATTERNS,
    SAFE_REGRESSION,
    SCRIPT_GRAYLIST,
    EvasionScenario,
    classify_interpreter_command,
)


class TestScenarioData:
    """Validate scenario data integrity."""

    def test_evasion_patterns_not_empty(self) -> None:
        assert len(EVASION_PATTERNS) >= 17

    def test_script_graylist_not_empty(self) -> None:
        assert len(SCRIPT_GRAYLIST) >= 7

    def test_safe_regression_not_empty(self) -> None:
        assert len(SAFE_REGRESSION) >= 9

    def test_all_evasion_blocked(self) -> None:
        for s in EVASION_PATTERNS:
            assert s.expected == "blocked", f"{s.command} should be blocked"

    def test_all_graylist_confirm(self) -> None:
        for s in SCRIPT_GRAYLIST:
            assert s.expected == "confirm", f"{s.command} should be confirm"

    def test_all_regression_safe(self) -> None:
        for s in SAFE_REGRESSION:
            assert s.expected == "safe", f"{s.command} should be safe"


class TestEvasionPatterns:
    """Verify evasion patterns cover all bypass techniques."""

    @pytest.mark.parametrize(
        "scenario",
        EVASION_PATTERNS,
        ids=[s.description for s in EVASION_PATTERNS],
    )
    def test_evasion_scenario(self, scenario: EvasionScenario) -> None:
        assert scenario.expected == "blocked"
        assert scenario.technique

    def test_covers_inline_interpreter(self) -> None:
        techniques = {s.technique for s in EVASION_PATTERNS}
        assert "inline_interpreter" in techniques

    def test_covers_eval(self) -> None:
        techniques = {s.technique for s in EVASION_PATTERNS}
        assert "eval" in techniques

    def test_covers_shell_indirection(self) -> None:
        techniques = {s.technique for s in EVASION_PATTERNS}
        assert "shell_indirection" in techniques

    def test_covers_base64(self) -> None:
        techniques = {s.technique for s in EVASION_PATTERNS}
        assert "base64" in techniques

    def test_covers_powershell(self) -> None:
        techniques = {s.technique for s in EVASION_PATTERNS}
        assert "powershell" in techniques

    def test_covers_crontab(self) -> None:
        techniques = {s.technique for s in EVASION_PATTERNS}
        assert "crontab" in techniques

    def test_covers_find_delete(self) -> None:
        techniques = {s.technique for s in EVASION_PATTERNS}
        assert "find_delete" in techniques


class TestScriptGraylist:
    """Verify script execution graylist covers major interpreters."""

    @pytest.mark.parametrize(
        "scenario",
        SCRIPT_GRAYLIST,
        ids=[s.description for s in SCRIPT_GRAYLIST],
    )
    def test_graylist_scenario(self, scenario: EvasionScenario) -> None:
        assert scenario.expected == "confirm"

    def test_covers_bash(self) -> None:
        cmds = {s.command.split()[0] for s in SCRIPT_GRAYLIST}
        assert "bash" in cmds

    def test_covers_python3(self) -> None:
        cmds = {s.command.split()[0] for s in SCRIPT_GRAYLIST}
        assert "python3" in cmds

    def test_covers_node(self) -> None:
        cmds = {s.command.split()[0] for s in SCRIPT_GRAYLIST}
        assert "node" in cmds


class TestSafeRegression:
    """Verify safe commands are not broken by hardening."""

    @pytest.mark.parametrize(
        "scenario",
        SAFE_REGRESSION,
        ids=[s.description for s in SAFE_REGRESSION],
    )
    def test_safe_scenario(self, scenario: EvasionScenario) -> None:
        assert scenario.expected == "safe"

    def test_version_checks_not_confused(self) -> None:
        """python3 --version must stay safe (not confused with python3 -c)."""
        version_cmds = [s for s in SAFE_REGRESSION if "--version" in s.command]
        assert len(version_cmds) >= 2
        for s in version_cmds:
            assert s.expected == "safe"

    def test_crontab_list_not_confused(self) -> None:
        """crontab -l must stay safe (not confused with crontab -r/-e)."""
        crontab_cmds = [s for s in SAFE_REGRESSION if "crontab" in s.command]
        assert len(crontab_cmds) >= 1
        for s in crontab_cmds:
            assert s.expected == "safe"


class TestClassifyInterpreterCommand:
    """Test the classify_interpreter_command stub."""

    def test_not_implemented(self) -> None:
        with pytest.raises(NotImplementedError):
            classify_interpreter_command("python3 -c 'import os'")
