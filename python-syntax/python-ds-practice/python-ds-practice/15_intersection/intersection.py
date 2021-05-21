def intersection(l1, l2):
    """Return intersection of two lists as a new list::

        >>> intersection([1, 2, 3], [2, 3, 4])
        [2, 3]

        >>> intersection([1, 2, 3], [1, 2, 3, 4])
        [1, 2, 3]

        >>> intersection([1, 2, 3], [3, 4])
        [3]

        >>> intersection([1, 2, 3], [4, 5, 6])
        []
    """

    lst1 = set(l1)
    lst2 = set(l2)
    common_numbers = lst1 & lst2
    return list(common_numbers)


intersection([1, 2, 3], [2, 3, 4])
