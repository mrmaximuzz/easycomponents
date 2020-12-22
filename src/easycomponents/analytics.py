"""Module for various components analysis"""

import itertools
from abc import abstractmethod, ABC
from dataclasses import dataclass
from typing import Collection, List

from .component import SimpleComponent


@dataclass
class AnalysisWarning(ABC):
    """Base class for the analysis warnings"""

    @abstractmethod
    def what(self) -> str:
        """Describes the warning in user-friendly format"""


@dataclass
class Duplicate(AnalysisWarning):
    """Error: multiple components with the same name"""

    name: str
    count: int

    def what(self) -> str:
        return f"'{self.name}' component occurs {self.count} times"


def find_dups(components: Collection[SimpleComponent]) -> List[Duplicate]:
    """Check a given collection for components with same names"""
    names = sorted(comp.name for comp in components)

    errs = []
    for name, group in itertools.groupby(names):
        count = len(list(group))
        if count > 1:
            errs.append(Duplicate(name, count))

    return errs


@dataclass
class Dangling(AnalysisWarning):
    """Error: component depends on inexistent one"""

    name: str
    dep: str

    def what(self) -> str:
        return f"'{self.name}' depends on '{self.dep}' which does not exist"


def find_dangling(components: Collection[SimpleComponent]) -> List[Dangling]:
    """Find inexistent dependencies for the components collection"""
    names = {comp.name for comp in components}

    errs = []
    for comp in components:
        for dep in comp.deps:
            if dep not in names:
                errs.append(Dangling(comp.name, dep))

    return errs
