"""Module for testing analytic implementation"""

from easycomponents.analytics import find_dups
from easycomponents.analytics import find_dangling
from easycomponents.analytics import Dangling, Duplicate

from easycomponents.component import SimpleComponent


def test_find_dups():
    """Test searching for duplicate names"""
    assert not find_dups([])

    comp1 = SimpleComponent("A", [])
    comp2 = SimpleComponent("B", [])
    assert not find_dups([comp1, comp2])

    comp1 = SimpleComponent("A", [])
    comp2 = SimpleComponent("A", [])
    assert find_dups([comp1, comp2]) == [Duplicate("A", 2)]

    comp1 = SimpleComponent("A", [])
    comp2 = SimpleComponent("A", [])
    comp3 = SimpleComponent("A", [])
    assert find_dups([comp1, comp2, comp3]) == [Duplicate("A", 3)]

    comp1 = SimpleComponent("A", [])
    comp2 = SimpleComponent("B", [])
    comp3 = SimpleComponent("A", [])
    comp4 = SimpleComponent("B", [])
    errs = [Duplicate("A", 2), Duplicate("B", 2)]
    assert find_dups([comp1, comp2, comp3, comp4]) == errs


def test_find_dangling():
    """Test for searching error dependencies"""

    comp1 = SimpleComponent("A", [])
    comp2 = SimpleComponent("B", [])
    assert not find_dangling([comp1, comp2])

    comp1 = SimpleComponent("A", ["B"])
    comp2 = SimpleComponent("B", [])
    assert not find_dangling([comp1, comp2])

    comp1 = SimpleComponent("A", [])
    comp2 = SimpleComponent("B", ["A"])
    assert not find_dangling([comp1, comp2])

    comp1 = SimpleComponent("A", ["X"])
    comp2 = SimpleComponent("B", [])
    errs = [Dangling("A", "X")]
    assert find_dangling([comp1, comp2]) == errs

    comp1 = SimpleComponent("A", ["X", "Y"])
    comp2 = SimpleComponent("B", [])
    errs = [Dangling("A", "X"), Dangling("A", "Y")]
    assert find_dangling([comp1, comp2]) == errs

    comp1 = SimpleComponent("A", ["X", "Y"])
    comp2 = SimpleComponent("B", ["Z"])
    errs = [Dangling("A", "X"), Dangling("A", "Y"), Dangling("B", "Z")]
    assert find_dangling([comp1, comp2]) == errs
