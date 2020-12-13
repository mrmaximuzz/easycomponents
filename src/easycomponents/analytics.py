"""Module for various components analysis"""

import itertools
from typing import List

from .component import SimpleComponent


def find_duplicates(components: List[SimpleComponent]) -> List[str]:
    """Check a list given for components with same names"""
    names = sorted(comp.name for comp in components)
    return [k for k, g in itertools.groupby(names) if len(list(g)) > 1]
