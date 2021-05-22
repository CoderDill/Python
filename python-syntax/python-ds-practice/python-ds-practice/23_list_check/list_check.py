def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """

    for ls in lst:
        if not type(ls) == list:
            return False
    return True

    # I found a lot of ways of how not to do it.
    # return bool(False for ls in lst if not type(ls) == list)
