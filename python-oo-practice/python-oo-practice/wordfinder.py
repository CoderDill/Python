import random


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    def __init__(self, path):
        """Opens path file and prints how many words were read."""
        dictionary = open(path)
        self.words = [w.strip() for w in dictionary]
        print(f"{len(self.words)} were read")

    def random(self):
        """Returns a random word"""
        return (random.choice(self.words))


class SpecialWordFinder(WordFinder):
    """Takes non-words or comments out"""

    def __init__(self, path):
        dictionary = super().__init__(open(path))
        self.words = [w.strip() for w in dictionary if w.strip()
                      and not w.startswith("#")]
