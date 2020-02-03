from itertools import chain, product
from operator import itemgetter

import pytest

from is_sorted import is_sorted


def generate_data(to):
    return chain(*(product(range(i), repeat=i) for i in range(1, to)))


@pytest.mark.parametrize("data", map(list, generate_data(6)))
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


@pytest.mark.parametrize("data,multi,result", [
    ([(1, 5), (1, 4), (1, 3), (1, 2), (1, 1)], [(itemgetter(0), False), (itemgetter(1), True)], True),
    ([(1, 5), (1, 4), (1, 3), (1, 2), (1, 4)], [(itemgetter(0), False), (itemgetter(1), True)], False),
    ([(1, 2), (1, 1), (2, 3), (2, 3), (3, 5)], [(lambda x: x[0], False), (lambda x: x[1], True)], True),
])
def test_multi_sorted(data, multi, result):
    assert is_sorted(data, multi=multi) is result


@pytest.mark.parametrize("data,key,reverse,multi", [
    ([1, 2, 3], None, True, [(lambda x: x, True)]),
    ([1, 2, 3], lambda x: x, False, [(lambda x: x, True)]),
    ([1, 2, 3], lambda x: x, True, [(lambda x: x, True)]),
])
def test_exception_raised(data, key, reverse, multi):
    with pytest.raises(ValueError) as exc_info:
        assert is_sorted(data, key=key, reverse=reverse, multi=multi)

    assert exc_info.value.args[0] == 'either key/reverse or multi must be specified'
