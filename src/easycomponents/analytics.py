"""Module for various components analysis"""

import itertools
from dataclasses import dataclass
from typing import Collection, List

from .component import ComponentGraph, SimpleComponent


@dataclass
class AnalysisWarning:
    """Base class for the analysis warnings"""

    def what(self) -> str:
        """Describes the warning in user-friendly format"""
        raise NotImplementedError


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


@dataclass
class BadComponents(Exception):
    """Base class for the errors in input components

    As python does not have Either monads, just use EAFP principle here
    """

    errs: List[AnalysisWarning]


def component_graph(comps: Collection[SimpleComponent]) -> ComponentGraph:
    """Validates input and create components graph

    Throws an exception if cannot construct valid graph
    """

    dups = find_dups(comps)
    dang = find_dangling(comps)

    if dups or dang:
        raise BadComponents([*dups, *dang])

    return {comp.name: comp for comp in comps}
