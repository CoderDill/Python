def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """

    num1_list = [int(num) for num in str(num1)]
    num2_list = [int(num) for num in str(num2)]

    return sum(num1_list) == sum(num2_list)


same_frequency(551122, 221515)
