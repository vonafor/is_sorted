import pytest

from is_sorted import _compare


@pytest.mark.parametrize("reverses,previous,current,result", [
    ((True,), (1,), (2,), False),
    ((True,), (2,), (1,), True),
    ((False,), (1,), (2,), True),
    ((False,), (2,), (1,), False),
    ((False,), (1,), (1,), True),
    ((True,), (1,), (1,), True),
])
def test_compare_with_single_comparison(reverses, previous, current, result):
    assert _compare(reverses, previous, current) is result


@pytest.mark.parametrize("reverses,previous,current,result", [
    # first keys equal, result depends on second keys
    ((False, True), (1, 1), (1, 2), False),
    ((False, True), (1, 2), (1, 1), True),
    ((False, False), (1, 1), (1, 2), True),
    ((False, False), (1, 2), (1, 1), False),
    ((False, False), (1, 1), (1, 1), True),
    ((False, True), (1, 1), (1, 1), True),

    # first keys not equal, result depends on first keys
    ((False, True), (1, 1), (2, 2), True),
    ((False, True), (1, 2), (2, 1), True),
    ((False, False), (1, 1), (2, 2), True),
    ((False, False), (1, 2), (2, 1), True),
    ((False, False), (1, 1), (2, 1), True),
    ((False, True), (1, 1), (2, 1), True),

    ((True, True), (1, 1), (2, 2), False),
    ((True, True), (1, 2), (2, 1), False),
    ((True, False), (1, 1), (2, 2), False),
    ((True, False), (1, 2), (2, 1), False),
    ((True, False), (1, 1), (2, 1), False),
    ((True, True), (1, 1), (2, 1), False),
])
def test_compare_with_multiple_comparison(reverses, previous, current, result):
    assert _compare(reverses, previous, current) is result


@pytest.mark.parametrize("reverses,previous,current,result", [
    ((True,), (1,), (2,), False),
    ((True,), (2,), (1,), True),
    ((False,), (1,), (2,), True),
    ((False,), (2,), (1,), False),
    ((False,), (1,), (1,), True),
    ((True,), (1,), (1,), True),
])
def test_compare_poor_classes(reverses, previous, current, result):
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

    assert _compare(reverses, tuple(map(A, previous)), tuple(map(A, current))) is result
    assert _compare(reverses, tuple(map(B, previous)), tuple(map(B, current))) is result
