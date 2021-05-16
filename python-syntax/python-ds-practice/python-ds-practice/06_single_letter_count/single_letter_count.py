def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?

        >>> single_letter_count('Hello World', 'h')
        1

        >>> single_letter_count('Hello World', 'z')
        0

        >>> single_letter_count("Hello World", 'l')
        3
    """
#Doesn't work and don't know why.
    # count = 0
    # for char in word:
    #     char.lower()
    #     if char == letter:
    #         count = count + 1
    # print(count)

#Does work and do know why.
    print(word.lower().count(letter.lower()))


single_letter_count("I hopepppp this works", "i")
