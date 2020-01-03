from operator import itemgetter

import pytest

from is_sorted import is_sorted


@pytest.mark.parametrize("elems,result", [
    ([1], True),
    ([1] * 10, True),
    ([1, 2, 3, 4, 2, 3], False),
    ([1, 2, 2, 3, 4, 4, 5], True),
    ([1, 2, 3, 4, 5], True),
    ([5, 4, 3, 2, 1], False),
    (sorted([2, 3, 1, 4, 5]), True),
    (sorted([2, 3, 1, 4, 5], reverse=True), False),
])
def test_straight(elems, result):
    assert is_sorted(elems) is result


@pytest.mark.parametrize("elems,result", [
    ([1], True),
    ([1] * 10, True),
    ([5, 5, 4, 3, 3, 2, 1, 1, 0, -1, -1], True),
    ([1, 2, 3, 4, 5], False),
    ([5, 4, 3, 2, 1], True),
    (sorted([2, 3, 1, 4, 5]), False),
    (sorted([2, 3, 1, 4, 5], reverse=True), True),
])
def test_reverse(elems, result):
    assert is_sorted(elems, reverse=True) is result


@pytest.mark.parametrize("elems,key,result", [
    ([(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)], itemgetter(0), True),
    ([(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)], itemgetter(1), False),
])
def test_straight_with_key(elems, key, result):
    assert is_sorted(elems, key=key) is result


@pytest.mark.parametrize("elems,key,result", [
    ([(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)], itemgetter(0), False),
    ([(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)], itemgetter(1), True),
])
def test_reverse_with_key(elems, key, result):
    assert is_sorted(elems, key=key, reverse=True) is result