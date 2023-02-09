from math import floor


def sqrt(x):
    if x < 0:
        raise ValueError("x must be non-negative")
    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1

    print(floor(guess))
    return guess


print(sqrt(8))
