tc = int(input())

for _ in range(tc):
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    count = 0
    for i in range(k):
        if a[i] > k:
            count += 1
    print(count)