"""Module for testing analytic implementation"""

from easycomponents.analytics import find_duplicates
from easycomponents.component import SimpleComponent


def test_check_duplicates():
    """Test searching for duplicate names"""
    assert not find_duplicates([])

    comp1 = SimpleComponent("A", [])
    comp2 = SimpleComponent("B", [])
    assert not find_duplicates([comp1, comp2])

    comp1 = SimpleComponent("A", [])
    comp2 = SimpleComponent("A", [])
    assert find_duplicates([comp1, comp2]) == ["A"]

    comp1 = SimpleComponent("A", [])
    comp2 = SimpleComponent("B", [])
    comp3 = SimpleComponent("A", [])
    assert find_duplicates([comp1, comp2, comp3]) == ["A"]
