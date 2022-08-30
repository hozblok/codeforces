from collections import deque
from decimal import Decimal


tc = int(input())

for _ in range(tc):
    n = int(input())
    s = input()
    if n == 1:
        print("0")
        continue
    m = (n // 2 + 1) if  n % 2 == 1 else n // 2
    sm = 0
    for i in range(m):
        if s[i] != "R":
            sm += i
        else:
            sm += n - i - 1
        # print(i, sm, s[i], s[i] == "R")
        if n % 2 == 1 and i == n // 2:
            pass
        else:
            if s[n - 1 - i] != "L":
                sm += i
            else:
                sm += n - i - 1
    k = n
    for i in range(m):
        if s[i] != "R":
            sm += n - (2 * i + 1)
            print(sm, end=" ")
            k -= 1
        if n % 2 == 1 and i == n // 2:
            pass
        else:
            if s[n - 1 - i] != "L":
                sm += n - (2 * i + 1)
                print(sm, end=" ")
                k -= 1
    while k:
        print(sm, end=" ")
        k -= 1
    print()
