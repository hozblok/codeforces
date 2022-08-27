tc = int(input())

for _ in range(tc):
    n, m = list(map(int, input().split()))
    if n == 1 and m == 1:
        print(0)
    elif m == 1 and n > 1:
        print(n)
    elif n == 1:
        print(m)
    else:
        print(n-1 + m-1 + 1 + min(m-1, n-1))
        