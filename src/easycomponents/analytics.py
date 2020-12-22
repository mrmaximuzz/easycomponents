"""Module for various components analysis"""

import itertools
from dataclasses import dataclass
from typing import Collection, List

from .component import SimpleComponent


@dataclass
class DepError:
    """Error in dependency: component depends on inexistent one"""

    component: str
    dependency: str


def find_duplicates(components: Collection[SimpleComponent]) -> List[str]:
    """Check a given collection for components with same names"""
    names = sorted(comp.name for comp in components)
    return [k for k, g in itertools.groupby(names) if len(list(g)) > 1]


def find_incorrect_deps(components: Collection[SimpleComponent]) -> List[DepError]:
    """Find inexistent dependencies for the components collection"""
    names = {comp.name for comp in components}

    errs = []
    for comp in components:
        for dep in comp.deps:
            if dep not in names:
                err = DepError(comp.name, dep)
                errs.append(err)

    return errs
