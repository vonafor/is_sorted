__all__ = ['is_sorted']

_empty = object()


def is_sorted(iterable, *, key=None, reverse=False):
    key = (lambda x: x) if key is None else key
    # expected that builtin sorted-function/sort-method uses only <
    # https://docs.python.org/3/howto/sorting.html#odd-and-ends
    # https://docs.python.org/3/library/stdtypes.html#list.sort
    if reverse:
        cmp = lambda a, b: not a < b
    else:
        cmp = lambda a, b: a < b or not b < a

    previous = _empty
    for current in map(key, iterable):
        if previous is not _empty:
            if not cmp(previous, current):
                return False
        previous = current
    return True
