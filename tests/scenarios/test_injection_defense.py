"""Tests for prompt injection defense and write-then-execute detection."""

from __future__ import annotations

import pytest

from chaos_auditor.scenarios.injection_defense import (
    detect_write_then_execute,
    extract_script_path,
    wrap_tool_output,
)


class TestWrapToolOutput:
    """Test output wrapping for prompt injection defense."""

    def test_not_implemented(self) -> None:
        with pytest.raises(NotImplementedError):
            wrap_tool_output("run_shell_command", "hello world")


class TestDetectWriteThenExecute:
    """Test write-then-execute detection."""

    def test_not_implemented(self) -> None:
        with pytest.raises(NotImplementedError):
            detect_write_then_execute("bash /tmp/evil.sh", {"/tmp/evil.sh"})

    def test_not_implemented_with_empty_set(self) -> None:
        with pytest.raises(NotImplementedError):
            detect_write_then_execute("bash /tmp/safe.sh", set())


class TestExtractScriptPath:
    """Test script path extraction."""

    def test_not_implemented(self) -> None:
        with pytest.raises(NotImplementedError):
            extract_script_path("bash /tmp/deploy.sh")
