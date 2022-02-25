"""
Module docstring
"""

j = [1, 2, 3]


def some_calculation(x, y):
    """method docstring
    :param x: something
    :param y: something
    :return: something
    """
    return x + y


def very_important_function(var1, var2, var3):
    """Applies `variables` to the `template` and writes to `file`."""
    with open(file, "w") as f:
        f.close()


if __name__ == "__main__":
    val = some_calculation(10, 15)
    val += 10
    print(f"number {val}")
