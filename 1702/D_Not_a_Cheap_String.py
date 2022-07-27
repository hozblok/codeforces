from collections import defaultdict
from string import ascii_lowercase

r = list(reversed(ascii_lowercase))
tc = int(input())

for _ in range(tc):
    s = input()
    price = int(input())
    sm = 0
    d = defaultdict(set)
    for i, c in enumerate(s):
        v = ord(c) - 96
        sm += v
        d[c].add(i)
    rr = iter(r)
    c = next(rr)
    while price < sm:
        if c in d:
            sm -= ord(c) - 96
            d[c].pop()
            if not d[c]:
                d.pop(c)
                c = next(rr)
        else:
            c = next(rr)
    res = "".join(c for i, c in enumerate(s) if c in d and i in d[c])
    print(res)
