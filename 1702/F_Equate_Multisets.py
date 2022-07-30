from collections import defaultdict


tc = int(input())


def reduce(cur: int):
    while cur % 2 == 0:
        cur //= 2
    return cur


for _ in range(tc):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    d = defaultdict(int)
    for el in a:
        cur = reduce(el)
        d[cur] += 1
    for el in b:
        cur = reduce(el)
        while cur >= 1:
            if cur in d and d[cur] > 0:
                d[cur] -= 1
                break
            else:
                cur //= 2

    for v in d.values():
        if v != 0:
            print("NO")
            break
    else:
        print("YES")
