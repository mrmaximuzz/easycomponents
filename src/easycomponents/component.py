"""
Software component description
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import List


@dataclass
class SimpleComponent:
    """The simplest component description: name and dependencies"""

    name: str
    deps: List[SimpleComponent]
