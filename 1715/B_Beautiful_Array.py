from decimal import Decimal
import math

tc = int(input())

for _ in range(tc):
    n, k, b, s = list(map(int, input().split()))
    res = []
    num = 0
    m = Decimal(s) / Decimal(k)
    if m < b:
        print(-1)
    elif b == 0:
        if k == 0:
            print(" ".join("0" for el in range(n)))
        elif k == 1:
            print(-1)
        elif k > 1:
            count = 0
            while count < s:
                res.append(k - 1)
                count += k -1
            while count > s:
                res[0] -= 1
                count -=1
            if len(res) > n:
                print(-1)
            else:
                print(" ".join(str(el) for el in reversed(res)))
    elif k == 1:
        if m == b:
            res.append(s)
            while len(res) < n:
                res.append(0)
            print(" ".join(str(el) for el in reversed(res)))
        else:
            print(-1)
    else:
        if math.floor(m) == b:
            res.append(s)
        else:
            factor = Decimal(m - b) * k
            num = math.floor(factor / Decimal(k - 1))
            res.append(s - num * (k - 1))
        if num > n - 1:
            print(-1)
        else:
            while num > 0:
                res.append(k - 1)
                num -= 1
            while len(res) < n:
                res.append(0)
            if len(res) > n:
                print(-1)
            print(" ".join(str(el) for el in reversed(res)))
