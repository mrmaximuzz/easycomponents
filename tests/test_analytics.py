"""Module for testing analytic implementation"""

from easycomponents.analytics import find_dups
from easycomponents.analytics import find_dangling
from easycomponents.analytics import Dangling, Duplicate

from easycomponents.component import SimpleComponent


def test_find_dups():
    """Test searching for duplicate names"""
    assert not find_dups([])

    comps = [
        SimpleComponent("A", []),
        SimpleComponent("B", []),
    ]
    assert not find_dups(comps)

    comps = [
        SimpleComponent("A", []),
        SimpleComponent("A", []),
    ]
    dups = [Duplicate("A", 2)]
    assert find_dups(comps) == dups

    comps = [
        SimpleComponent("A", []),
        SimpleComponent("A", []),
        SimpleComponent("A", []),
    ]
    dups = [Duplicate("A", 3)]
    assert find_dups(comps) == dups

    comps = [
        SimpleComponent("A", []),
        SimpleComponent("B", []),
        SimpleComponent("A", []),
        SimpleComponent("B", []),
    ]
    errs = [Duplicate("A", 2), Duplicate("B", 2)]
    assert find_dups(comps) == errs


def test_find_dangling():
    """Test for searching error dependencies"""

    assert not find_dangling([])

    comps = [
        SimpleComponent("A", []),
        SimpleComponent("B", []),
    ]
    assert not find_dangling(comps)

    comps = [
        SimpleComponent("A", ["B"]),
        SimpleComponent("B", []),
    ]
    assert not find_dangling(comps)

    comps = [
        SimpleComponent("A", []),
        SimpleComponent("B", ["A"]),
    ]
    assert not find_dangling(comps)

    comps = [
        SimpleComponent("A", ["X"]),
        SimpleComponent("B", []),
    ]
    errs = [Dangling("A", "X")]
    assert find_dangling(comps) == errs

    comps = [
        SimpleComponent("A", ["X", "Y"]),
        SimpleComponent("B", []),
    ]
    errs = [Dangling("A", "X"), Dangling("A", "Y")]
    assert find_dangling(comps) == errs

    comps = [
        SimpleComponent("A", ["X", "Y"]),
        SimpleComponent("B", ["Z"]),
    ]
    errs = [Dangling("A", "X"), Dangling("A", "Y"), Dangling("B", "Z")]
    assert find_dangling(comps) == errs
