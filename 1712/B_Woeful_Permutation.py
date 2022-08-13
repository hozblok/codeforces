tc = int(input())

for _ in range(tc):
    n = int(input())
    res = []
    cur = -1
    for i in range(n, 0, -1):
        res.append(i + cur if i + cur > 0 else 1)
        cur *= -1
    print(" ".join((str(el) for el in reversed(res))))
