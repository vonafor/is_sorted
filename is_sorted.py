__version__ = '0.0.1'


def is_sorted(iterable, *, key=None, reverse=False):
    """
    Return True if all items from the iterable are sorted in ascending order.
    Custom sort order can be checked by passing key function.
    Descending order can be checked by setting reverse flag.
    """
    key = (lambda x: x) if key is None else key
    # expected that builtin sorted-function/sort-method uses only <
    # https://docs.python.org/3/howto/sorting.html#odd-and-ends
    # https://docs.python.org/3/library/stdtypes.html#list.sort
    if reverse:
        cmp = lambda a, b: not a < b
    else:
        cmp = lambda a, b: a < b or not b < a

    is_first = True
    previous = None
    for current in map(key, iterable):
        if is_first:
            is_first = False
        else:
            if not cmp(previous, current):
                return False
        previous = current
    return True
