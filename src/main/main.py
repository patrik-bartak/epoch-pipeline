"""
Module docstring
"""


def some_calculation(x, y):
    """
    method docstring
    :param x: something
    :param y: something
    :return: something
    """
    return x + y


if __name__ == "__main__":
    VAL = some_calculation(10, 15)
    VAL += 10
    print(f"number {VAL}")
