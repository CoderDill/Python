def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?

        >>> single_letter_count('Hello World', 'h')
        1

        >>> single_letter_count('Hello World', 'z')
        0

        >>> single_letter_count("Hello World", 'l')
        3
    """

    count = 0
    lower_words = word.lower()

    for char in lower_words:
        if char == letter:
            count = count + 1
    print(count)

#Alternate solution: 
    # return print(word.lower().count(letter.lower()))


single_letter_count("I hopepppp this works", "i")
