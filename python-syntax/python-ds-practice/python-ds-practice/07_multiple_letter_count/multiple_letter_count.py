def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """

    phrase.lower()
    count = 0

    for char in phrase:
        count = count + 1
    
    return print({char: count})


multiple_letter_count("I like working on a new one.")
