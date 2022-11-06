pn = int(input())

for _ in range(pn):
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print("YES")
    else:
        print("YES" if a[0] == 1 else "NO")