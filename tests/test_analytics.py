"""Module for testing analytic implementation"""

from easycomponents.analytics import find_duplicates
from easycomponents.analytics import find_incorrect_deps
from easycomponents.analytics import DepError

from easycomponents.component import SimpleComponent


def test_find_duplicates():
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


def test_find_incorrect_deps():
    """Test for searching error dependencies"""

    comp1 = SimpleComponent("A", [])
    comp2 = SimpleComponent("B", [])
    assert not find_incorrect_deps([comp1, comp2])

    comp1 = SimpleComponent("A", ["B"])
    comp2 = SimpleComponent("B", [])
    assert not find_incorrect_deps([comp1, comp2])

    comp1 = SimpleComponent("A", [])
    comp2 = SimpleComponent("B", ["A"])
    assert not find_incorrect_deps([comp1, comp2])

    comp1 = SimpleComponent("A", ["X"])
    comp2 = SimpleComponent("B", [])
    errs = [DepError("A", "X")]
    assert find_incorrect_deps([comp1, comp2]) == errs

    comp1 = SimpleComponent("A", ["X", "Y"])
    comp2 = SimpleComponent("B", [])
    errs = [DepError("A", "X"), DepError("A", "Y")]
    assert find_incorrect_deps([comp1, comp2]) == errs

    comp1 = SimpleComponent("A", ["X", "Y"])
    comp2 = SimpleComponent("B", ["Z"])
    errs = [DepError("A", "X"), DepError("A", "Y"), DepError("B", "Z")]
    assert find_incorrect_deps([comp1, comp2]) == errs
