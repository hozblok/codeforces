import math

tc = int(input())

for _ in range(tc):
    n = int(input())
    m1 = float('+inf')
    m2 = float('+inf')
    m12 = float('+inf')
    for __ in range(n):
        m, books = list(map(int, input().split()))
        m = int(m)
        if books == 11 and m12 > m:
            m12 = m
        elif books == 10 and m1 > m:
            m1 = m
        elif books == 1 and m2 > m:
            m2 = m

    res = min(m1 + m2, m12)
    print(res if math.isfinite(res) else -1)
