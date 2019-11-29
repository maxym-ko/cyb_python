import math


def func(x):
    return 0.25 * math.log((1 + x) / (1 - x)) + 0.5 * math.atan(x)


x = float(input('... '))
print(func(x))