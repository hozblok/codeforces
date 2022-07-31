tc = int(input())

for _ in range(tc):
    n, m = list(map(int, input().split()))
    a = list(sorted(map(int, input().split())))
    if n == m:
        print(m)
        continue
    elif n == m + 1 or n == m + 2:
        print(n - 1)
        continue
    gaps = []
    prev = 0
    res_un = 0
    for el in a:
        if prev == 0:
            g = n - a[-1] + el - 1
        else:
            g = el - prev - 1
        if g > 0:
            gaps.append(g)
        prev = el
    gaps.sort(reverse=True)
    for j, el in enumerate(gaps):
        red = max(el - (4 * j), 0)
        if red > 1:
            red -= 1
        res_un += red
    print(n - res_un)
