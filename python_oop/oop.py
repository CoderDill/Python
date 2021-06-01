from collections import Counter

my_counter = Counter("OOMPA LOOMPA")

most_common = my_counter.most_common()


class Triangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
