"""
Software component description
"""

from dataclasses import dataclass
from typing import List


@dataclass
class SimpleComponent:
    """The simplest component description: name and dependencies

    name: unique component's identifier, acts as a key in storages
    deps: list of dependencies referenced by name
    """

    name: str
    deps: List[str]
