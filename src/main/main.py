"""
Module docstring
"""


def some_calculation(x, y):
    """method docstring
    :param x: something
    :param y: something
    :return: something
    """
    return x + y


if __name__ == "__main__":
    val = some_calculation(10, 15)
    val += 10
    print(f"number {val}")
