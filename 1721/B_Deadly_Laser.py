tc = int(input())

for _ in range(tc):
    n, m, sx, sy, d = list(map(int, input().split()))
    if sx - d > 1 and sy + d < m or sx + d < n and sy - d > 1:
        print(n - 1 + m - 1)
    else:
        print(-1)
