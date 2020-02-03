__version__ = '0.0.2'

__all__ = ['is_sorted']


def _compare(reverses, previous, current):
    # expected that builtin sorted-function/sort-method uses only <
    # https://docs.python.org/3/howto/sorting.html#odd-and-ends
    # https://docs.python.org/3/library/stdtypes.html#list.sort
    for reverse, a, b in zip(reverses, previous, current):
        if reverse:
            if a < b:
                return False
            if a > b:
                return True
        else:
            if a > b:
                return False
            if a < b:
                return True
    return True


def is_sorted(iterable, *, key=None, reverse=False, multi=None):
    """
    Return True if all items from the iterable are sorted in ascending order.
    Custom sort order can be checked by passing key function.
    Descending order can be checked by setting reverse flag.

    Multiple keys sorting with custom order can be checking by setting
    multi argument with following format: [(key1, reverse1), ..., (keyN, reverseN)]
    Raises ValueError if key/reverse is specified alongside with multi.

    Examples:
        >>> is_sorted([1, 2, 3, 4, 5, 6])
        True
        >>> is_sorted([5, 4, 3, 2, 1], reverse=True)
        True
        >>> is_sorted([1, 2, 3], key=lambda x: -x)
        False
        >>> is_sorted([(1, 2), (1, 1), (2, 3), (2, 3), (3, 5)], multi=[(lambda x: x[0], False), (lambda x: x[1], True)])
        True
    """
    if multi and (key or reverse):
        raise ValueError('either key/reverse or multi must be specified')

    if not multi:
        key = (lambda x: x) if not key else key
        multi = [(key, reverse)]
    keys, reverses = list(zip(*multi))

    is_first = True
    previous = None
    for current in map(lambda x: tuple(k(x) for k in keys), iterable):
        if is_first:
            is_first = False
        else:
            if not _compare(reverses, previous, current):
                return False
        previous = current
    return True
