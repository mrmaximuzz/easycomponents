"""
Software component description
"""

from dataclasses import dataclass
from typing import Dict, List


@dataclass
class SimpleComponent:
    """The simplest component description: name and dependencies

    name: unique component's identifier, acts as a key in storages
    deps: list of dependencies referenced by name
    """

    name: str
    deps: List[str]


@dataclass
class Instability:
    """Identify the component's instability

    Instability is a simple metric which is defined as amount of output
    dependencies divided by total amount of dependencies. The main instability
    rule is: no component should depend on other component with higher
    instablility value.

    deps_in: amount of components that depend on this one
    deps_out: amount of dependencies of this component
    """

    deps_in: int
    deps_out: int

    def ratio(self) -> float:
        """Return the instability value as a float ratio"""
        return self.deps_out / (self.deps_out + self.deps_in)


# in component graph all nodes are accessed by its names
ComponentGraph = Dict[str, SimpleComponent]
