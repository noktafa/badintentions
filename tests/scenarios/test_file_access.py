"""Tests for file access safety scenarios."""

from __future__ import annotations

import pytest

from chaos_auditor.scenarios.file_access import (
    READ_BLOCKED_PATHS,
    WRITE_BLOCKED_PATHS,
    FileAccessScenario,
    check_read_safety,
    check_write_safety,
)


class TestScenarioData:
    """Validate scenario data integrity."""

    def test_read_blocked_not_empty(self) -> None:
        assert len(READ_BLOCKED_PATHS) >= 4

    def test_write_blocked_not_empty(self) -> None:
        assert len(WRITE_BLOCKED_PATHS) >= 6

    def test_all_read_blocked_have_correct_operation(self) -> None:
        for s in READ_BLOCKED_PATHS:
            assert s.operation == "read"
            assert s.expected == "blocked"

    def test_all_write_blocked_have_correct_operation(self) -> None:
        for s in WRITE_BLOCKED_PATHS:
            assert s.operation == "write"
            assert s.expected == "blocked"

    def test_all_paths_are_absolute(self) -> None:
        for s in READ_BLOCKED_PATHS + WRITE_BLOCKED_PATHS:
            assert s.path.startswith("/"), f"Path {s.path} is not absolute"


class TestReadBlocked:
    """Verify read-blocked paths cover sensitive files."""

    @pytest.mark.parametrize(
        "scenario",
        READ_BLOCKED_PATHS,
        ids=[s.description for s in READ_BLOCKED_PATHS],
    )
    def test_read_blocked_scenario(self, scenario: FileAccessScenario) -> None:
        assert scenario.expected == "blocked"

    def test_covers_credentials(self) -> None:
        cats = {s.category for s in READ_BLOCKED_PATHS}
        assert "credentials" in cats

    def test_covers_keys(self) -> None:
        cats = {s.category for s in READ_BLOCKED_PATHS}
        assert "keys" in cats


class TestWriteBlocked:
    """Verify write-blocked paths cover critical system files."""

    @pytest.mark.parametrize(
        "scenario",
        WRITE_BLOCKED_PATHS,
        ids=[s.description for s in WRITE_BLOCKED_PATHS],
    )
    def test_write_blocked_scenario(self, scenario: FileAccessScenario) -> None:
        assert scenario.expected == "blocked"

    def test_covers_system_config(self) -> None:
        cats = {s.category for s in WRITE_BLOCKED_PATHS}
        assert "system_config" in cats

    def test_covers_system_binaries(self) -> None:
        cats = {s.category for s in WRITE_BLOCKED_PATHS}
        assert "system_binaries" in cats

    def test_covers_system_boot(self) -> None:
        cats = {s.category for s in WRITE_BLOCKED_PATHS}
        assert "system_boot" in cats


class TestFunctions:
    """Test function stubs."""

    def test_check_read_safety_not_implemented(self) -> None:
        with pytest.raises(NotImplementedError):
            check_read_safety("/etc/shadow")

    def test_check_write_safety_not_implemented(self) -> None:
        with pytest.raises(NotImplementedError):
            check_write_safety("/etc/passwd")
