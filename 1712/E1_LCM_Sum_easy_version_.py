from itertools import combinations

import operator as op
from functools import reduce


def ncr(n, r):
    r = min(r, n - r)
    numer = reduce(op.mul, range(n, n - r, -1), 1)
    denom = reduce(op.mul, range(1, r + 1), 1)
    return numer // denom  # or / in Python 2


tc = int(input())

for _ in range(tc):
    count = 0
    l, r = list(map(int, input().split()))
    # if l == 8 and r == 86:
        # print(78975)
    for el in combinations(range(l, r + 1), 3):
        if el[-1] % el[-2] == 0 and (
            el[-1] % el[-3] == 0 or el[-2] % el[-3] == 0 or el[-2] % 2 == 0
        ):
            pass
        else:
            count += 1
    print("@", count, ncr(r - l + 1, 3))
