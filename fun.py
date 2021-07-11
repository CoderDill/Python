from unittest import TestCase

# from mondrian_art import generate
# plt = generate()
# plt.show()

# num = 0

# while num <= 100:
#     print(num)
#     num += 10

# print("ALL DONE")


# target = 37
# guess = None

# while guess != target:
#     guess = input("Please enter a guess..")
#     if guess == "q" or guess == "quit":
#         break
#     guess = int(guess)

# print("alldone")

# scores = [45, 99, 100, 49]

# if 45 in scores:

#     vegan_no_nos = ["eggs", "meat", "fish"]

#     pie_ingredients = ["sugar", "eggs"]

#     for food in pie_ingredients:
#         if food in vegan_no_nos:
#             print(f"You cannot eat {food}")
#         else:
#             print(f"You can eat {food}")

# nums = range(0, 100)

def adder(x, y):
    """Adds two nums together.

    >>>adder(3,5)
    8
    """

    return x + y


class AdderTestCase(TestCase):
    """Unit Tests."""

    def test_adder(self):
        self.assertEqual(adder(2, 5),  7)


def reverse_str(s):
    return s[::-1]


def is_palindrome(s):
    rev = reverse_str(s)
    return s.lower() == rev.lower()


def factorial(n):
    if not (isinstance(n, int) and n >= 0):
        raise ValueError("'n' must be a non-negative integer.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
