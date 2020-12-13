"""Module for testing analytic implementation"""

from easycomponents.analytics import check_duplicates
from easycomponents.component import SimpleComponent


def test_check_duplicates():
    """Test searching for duplicate names"""
    assert check_duplicates([]) == []  # extreme case

    comp1 = SimpleComponent("A", [])
    comp2 = SimpleComponent("B", [])
    assert check_duplicates([comp1, comp2]) == []

    comp1 = SimpleComponent("A", [])
    comp2 = SimpleComponent("A", [])
    assert check_duplicates([comp1, comp2]) == ["A"]

    comp1 = SimpleComponent("A", [])
    comp2 = SimpleComponent("B", [])
    comp3 = SimpleComponent("A", [])
    assert check_duplicates([comp1, comp2, comp3]) == ["A"]
