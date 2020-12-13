"""Module for various components analysis"""

import itertools
from dataclasses import dataclass
from typing import List

from .component import SimpleComponent


@dataclass
class DepError:
    """Error in dependency"""

    component: str
    dependency: str


def find_duplicates(components: List[SimpleComponent]) -> List[str]:
    """Check a list given for components with same names"""
    names = sorted(comp.name for comp in components)
    return [k for k, g in itertools.groupby(names) if len(list(g)) > 1]


def find_incorrect_deps(components: List[SimpleComponent]) -> List[DepError]:
    """Find inexistent dependencies for the components list"""
    names = {comp.name for comp in components}

    errs = []
    for comp in components:
        for dep in comp.deps:
            if dep not in names:
                err = DepError(comp.name, dep)
                errs.append(err)

    return errs
