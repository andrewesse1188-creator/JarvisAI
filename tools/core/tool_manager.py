"""
Compatibilidad con versiones anteriores.

El ToolManager oficial vive en:

tools.core.manager
"""

from tools.core.manager import (
    ToolManager,
    tool_manager,
)

__all__ = [
    "ToolManager",
    "tool_manager",
]
