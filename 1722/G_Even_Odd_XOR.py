import enum
from functools import reduce
import operator


tc = int(input())


for _ in range(tc):
    n = int(input())
    if n == 3:
        print("2 1 3")
        continue
    a = []
    b = []
    val = 1
    for i in range(n // 2):
        a.append(val)
        val += 1
        b.append(val)
        val += 1
    if n % 2 == 0:
        b.pop()
    a_xor = reduce(operator.xor, a)
    b_xor = reduce(operator.xor, b)
    ax = f"{a_xor:031b}"
    bx = f"{b_xor:031b}"
    last = []
    for i, el in enumerate(ax):
        bel = bx[i]
        if el == "0":
            last.append("1" if bel == "1" else "0")
        else:
            last.append("1" if bel == "0" else "0")
    res_last = int("".join(last))
    if n % 2 == 0:
        b.append(res_last)
    else:
        a, b = b, a
        a.append(res_last)
    # print(f"{n=}")
    # print(f"{a=} {b=}")
    # print(a_xor, b_xor ^ res_last)
    while a and b:
        print(a.pop(), end=" ")
        print(b.pop(), end=" ")
    print()

    # res = [0] * n
    # val = 1
    # prev1 = None
    # a1, a2 = 0, 0
    # for i in range(0, n, 2):
    #     res[i] = val
    #     prev1 = a1
    #     a1 ^= val
    #     val += 1
    # prev2 = None
    # for i in range(1, n, 2):
    #     res[i] = val
    #     prev2 = a2
    #     a2 ^= val
    #     val += 1
    # a = None
    # prev = None
    # if n % 2 == 1:
    #     a = f"{a1:b}"
    #     prev = f"{prev2:b}"
    # else:
    #     a = f"{a2:b}"
    # a = "0" * (31 - len(a)) + a
    # ares = f"{prev:b}"
    # print(" ".join(map(str, res)))
    # print(a1, a2)
    # print(f"{prev1:b}", f"{prev2:b}")
    # print()
