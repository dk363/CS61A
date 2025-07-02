def width(area, height):
    assert area % height == 0
    return area // height

def perimeter(width, height):
    return 2 * (width + height)

def divisors(n):
    return [1] + [x for x in range(2, n) if n % x == 0]

def min_perimeter(area):
    heights = divisors(area)
    perimeters = [perimeter(width(area, h), h) for h in heights]
    return min(perimeters)

def apply_to_all(map_fn, s):
    return [map_fn(x) for x in s]

def keep_if(filter_fn, s):
    return [x for x in s if filter_fn]

def reduce(reduce_fn, s, initial):
    reduced = initial
    for x in s:
        reduced = reduce_fn(reduced, x)
    return reduced

def divisors_of(n):
    divides_n = lambda x : n % x == 0
    return [1] + keep_if(divides_n, range(2, n))

def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'fen zhi bi xu shi shu '
    return [root_label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False # 检查树是否是一个list且长度大于等于1
    for branch in branches(tree):
        if not is_tree(branch):
            return False # 检查分支是否是树，保证树的结构良好
    return True

def is_leaf(tree): # 检查是否有分支，若无分支就是叶子
    return not branches(tree)


def add_rationals(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + ny *dx, dx * dy)

def mul_rational(x, y):
    return rational(numer(x) * numer(y), denom(x) * denom(y))

def print_rational(x):
    print(numer(x), '/', denom(x))

def rationals_are_equal(x, y):
    return numer(x) * denom(y) == numer(y) * denom(x)

def rational(x, y):
    return [x, y]

def numer(x):
    return x[0]

def denom(x):
    return x[1]

from fractions import gcd

def rational(n, d):
    g = gcd(n, d)
    return [n//g, d//g]

def square_rational(x):
    return mul_rational(x, x)

def pair(x, y):
    def get(index):
        if index == 0:
            return x
        elif index == 1:
            return y
    return get

def select(p, i):
    return p(i)

from datetime import date

tues = date(2014, 5, 13)

print(date(2014, 5, 19) - tues)

print(tues.year)

print(tues.strftime('%A, %B %d'))

print('1234'.isnumeric())

chinese = ['coin', 'string', 'myriad']
suits = chinese
suits.pop()
suits.remove('coin')
suits.append('cup')
suits.extend(['sword', 'club'])
suits[2] = 'sqade'
print(suits)
