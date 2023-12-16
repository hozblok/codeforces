from collections import defaultdict
tc = int(input())

for _ in range(tc):
    d = defaultdict(set)
    n = int(input())
    d_start = dict()
    for el in range(n-1):
        res = input.split()
        a = int(res[0])
        b = int(res[1])
        d[a].add(b)
        d[b].add(a)
    for k, v in d.items():
        if len(d[k]) == 1:
            ...