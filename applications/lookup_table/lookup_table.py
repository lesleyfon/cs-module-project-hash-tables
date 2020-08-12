# Your code here
import random
import math
from time import time


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v


dictionary = {}

_s = time()


def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """

    key = f'{x}{y}'

    if key in dictionary and dictionary[key] is not None:
        return dictionary[key]
    else:

        dictionary[f'{x}{y}'] = slowfun_too_slow(x, y)
        return dictionary[f'{x}{y}']
    # Your code here


# Do not modify below this line!
for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)

    print(f'{i}: {x},{y}: {slowfun(x, y)}')

print(f'{time() - _s:.5f}')
