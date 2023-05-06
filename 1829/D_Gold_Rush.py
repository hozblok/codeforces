tc = int(input())

def dev(a):
    x = a // 3
    y = a - (a // 3)
    return (x, y) if (a % 3 == 0) else (-1, -1)

def check(x, a, b):
    while x > 0:
        if x == b:
            return True
        else:
            x1, x2 = dev(x)
            # x1 = (2 * x // 3) if ((2 * x) % 3) == 0 else -1
            # x2 = (a - x1) if x1 > 0 else -1
            return check(x1, a, b) or check(x2, a, b)
    return False


for _ in range(tc):
    a, b = list(map(int, input().split()))
    if b > a:
        print("NO")
        continue
    if b == a:
        print("YES")
        continue
    res = check(a, a, b)
    print("YES" if res else "NO")
    # x = a // 3 if (a % 3 == 0) else -1
    # while x > 0:
    #     print("@x", x, b)
    #     if x == b:
    #         res = "YES"
    #         break
    #     else:
    #         x = (2 * x // 3) if ((2 * x) % 3) == 0 else -1
    # if not res:
    #     y = a - (a // 3) if (a % 3 == 0) else -1
    #     while y > 0:
    #         print("@y", y, b)
    #         if y == b:
    #             res = "YES"
    #             break
    #         else:
    #             y = (2 * y // 3) if ((2 * y) % 3) == 0 else -1
    # print(res if res else "NO")
