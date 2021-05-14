def print_upper_words(words):
    """takes a list of words and returns them in all UPPERCASE"""

    for word in words:
        print(word.upper())


def print_upper_words_two(words):
    """takes a list of words and returns only the words 
            that start with an 'e' in all UPPERCASE"""

    for word in words:
        if word.startswith('e') or word.startswith("E"):
            print(word.upper())


def print_upper_words_three(words, starts_with):
    """takes a list of words and a set of letters a user inputs
            and prints only the words that start with those letters"""

    for word in words:
        for char in starts_with:
            if word.startswith(char):
                print(word.upper())


print_upper_words_three(["hello", "hey", "goodbye", "yo", "yes"],
                        starts_with={"h", "y"})
