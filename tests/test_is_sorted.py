import itertools

import pytest

from is_sorted import is_sorted


@pytest.mark.parametrize("data", map(list, itertools.product(range(5), repeat=5)))
def test_is_sorted(data):
    sorted_ = sorted(data)
    reverse_sorted = sorted(data, reverse=True)
    assert is_sorted(data) is (data == sorted_)
    assert is_sorted(data, reverse=True) is (data == reverse_sorted)


@pytest.mark.parametrize("data", [
    [],
    (),
    '',
    range(0),
    [1],
    (1,),
    'a',
    range(1),
])
def test_degenerate_cases(data):
    assert is_sorted(data) is True
    assert is_sorted(data, reverse=True) is True


@pytest.mark.parametrize("data,reverse,result", [
    ([1, 2, 3], False, True),
    ([2, 1, 3], True, False),
    ([2, 1, 3], False, False),
    ([3, 2, 1], True, True),
])
def test_with_key(data, reverse, result):
    class A:
        def __init__(self, i):
            self.i = i

    data = [A(i) for i in data]
    assert is_sorted(data, key=lambda d: d.i, reverse=reverse) is result


@pytest.mark.parametrize("data,reverse,result", [
    ([1, 2, 3], False, True),
    ([1, 2, 3], True, False),
    ([3, 2, 1], True, True),
    ([3, 2, 1], False, False),
])
def test_poor_comparison_classes(data, reverse, result):
    class A:
        def __init__(self, i):
            self.i = i

        def __lt__(self, other):
            return self.i < other.i

    class B:
        def __init__(self, i):
            self.i = i

        def __gt__(self, other):
            return self.i > other.i

    assert is_sorted([A(d) for d in data], reverse=reverse) is result
    assert is_sorted([B(d) for d in data], reverse=reverse) is result
