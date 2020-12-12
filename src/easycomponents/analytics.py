"""Module for various components analysis"""

from typing import List

from .component import SimpleComponent


def check_duplicates(components: List[SimpleComponent]):
    """Check a list given for a components with same names"""
    names = {comp.name for comp in components}
    return len(names) == len(components)
