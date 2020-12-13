"""Module for various components analysis"""

from typing import List

from .component import SimpleComponent


def check_duplicates(components: List[SimpleComponent]) -> List[str]:
    """Check a list given for components with same names"""
    duplicates = set()

    names = sorted(comp.name for comp in components)
    for name, other in zip(names[:-1], names[1:]):
        if name == other:
            duplicates.add(name)

    return sorted(duplicates)
