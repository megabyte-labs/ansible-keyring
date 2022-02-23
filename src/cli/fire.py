import fire


class Calculator(object):
    """A simple calculator class."""

    def sum(self, a: int, b: int):
        """
        Sums of two numbers

        Args:
            a (int): first number
            b (int): second number

        Returns:
            int: results
        """
        return a + b


if __name__ == "__main__":
    # Fire creates a CLI from the Calculator class
    fire.Fire(Calculator)
