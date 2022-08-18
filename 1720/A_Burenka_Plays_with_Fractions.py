from decimal import Decimal


tc = int(input())

for _ in range(tc):
    a, b, c, d = list(map(int, input().split()))
    # print(a/b, c/d)
    if Decimal(a)/b == Decimal(c)/d:
        print(0)
    elif a == 0 and c != 0:
        print(1)
    elif a != 0  and c == 0:
        print(1)
    elif a == c == 0:
        print(0)
    # elif b == d:
    #     if a % c == 0 or c % a == 0:
    #         print(1)
    #     else:
    #         print(2)
    elif (c * b) % (d * a) == 0:
        print(1)
    elif (d * a) % (c * b) == 0:
        print(1)
    else:
        print(2)