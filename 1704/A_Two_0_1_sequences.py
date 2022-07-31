tc = int(input())

for _i in range(tc):
    res = True
    n, m = [int(el) for el in input().split()]
    a = list(reversed(input()))
    b = reversed(input())
    rep = None
    for j, el in enumerate(b):
        v = a[j]
        if el != v:
            if j == m - 1:
                rep = el
                break
            else:
                res = False
                break
    if rep is not None:
        res = rep in a[m:]
    print("YES" if res else "NO")
