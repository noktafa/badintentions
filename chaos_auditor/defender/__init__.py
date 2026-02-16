"""Defender integration — monitoring and response tracking.

Provides hooks for defensive systems to observe audit activity
and measure detection/response capabilities.
"""

from chaos_auditor.defender.monitor import DefenderMetrics, DefenderMonitor, DetectionEvent

__all__ = [
    "DefenderMetrics",
    "DefenderMonitor",
    "DetectionEvent",
]
