import random
import functools


print('Enter number of digits.')
N = int(input())
nums = []
for i in range(N):
    nums.append(random.randint(1, 9))

un_set = {}  # empty set for union func
r = []  # empty list for reverse func

# filters


def odds(x):
    if x % 2 == 1:
        return x


def evens(x):
    if x % 2 == 0:
        return x


def simples(x):
    if x == 1 or 2 or 3 or 5 or 7:
        return x


# mappers


def negated(x):
    return - x


def inverted(x):
    return 1/x


def squared(x):
    return x**2


# reducers


def sum(x, x_next):
    return x + x_next


def multiply(x, x_next):
    return x * x_next


def join(x, x_next):
    return x*10 + x_next


def unite(*args):
    un_set.add(*args)
    return un_set


def reverse(x):
    r.insert(0, x)
    return r


print('Choose actions.')
actions = input()
rd, mp, fl = actions.split(' ')

fn = {'odds': odds,
      'evens': evens,
      'simples': simples,
      'negated': negated,
      'inverted': inverted,
      'squared': squared,
      'sum': sum,
      'multiply': multiply,
      'join': join,
      'unite': unite,
      'reverse': reverse
      }

print(functools.reduce(fn[rd], [*map(fn[mp], [*filter(fn[fl], nums)])]))
