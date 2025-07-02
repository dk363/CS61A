def search(f):
    x = 0
    while True:
        if f(x):
            return x
        x += 1


def square(x):
    return x * x

def positive(x):
    return max(0, square(x) - 100)
# 0 is False

def inverse(f):
    return lambda y: search(lambda x: f(x) == y)
