tc = int(input())

for _ in range(tc):
    n = int(input())
    if n == 1:
        print(1)
    else:
        print(n // 2 + n % 2)