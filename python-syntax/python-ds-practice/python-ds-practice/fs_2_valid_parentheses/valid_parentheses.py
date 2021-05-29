def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    # I don't understand how this function works for the
    # last two tests.
    count = 0

    for par in parens:
        if par == "(":
            count += 1
        elif par == ")":
            count -= 1

        if count < 0:
            return False

    return count == 0


valid_parentheses("((())")
