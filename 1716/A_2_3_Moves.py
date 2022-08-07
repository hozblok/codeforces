tc = int(input())

for _ in range(tc):
    n = int(input())
    if n < 2:
        print(2)
    elif n == 2:
        print(1)
    elif n == 3:
        print(1)
    elif n == 4:
        print(2)
    elif n % 3 == 0:
        print(n // 3)
    elif n % 3 >= 1:
        print((n // 3) + 1)
