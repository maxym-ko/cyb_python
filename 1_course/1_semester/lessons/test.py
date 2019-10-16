def func(x):
    res = None
    if x <= 5:
        res = 0
    elif x < 3:
        res = 2 * x
    elif x <= 7:
        res = x + 2
    else:
        res = x
    return res


print(float('inf'))
print(float('-inf'))
print(float('nan'))
