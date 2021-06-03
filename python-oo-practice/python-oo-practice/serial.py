"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """Make a serial number generator starting at start."""
        self.start = self.next = start

    def generate(self):
        """Return next serial number."""
        self.next = self.next + 1
        return self.next - 1

    def reset(self):
        """Reset generator back to start."""
        self.next = self.start
