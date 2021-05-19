def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    letter_count = {}

    for ltr in phrase:
        letter_count[ltr] = letter_count.get(ltr, 0) + 1

    return letter_count


multiple_letter_count("I like working on a new one.")
