from functools import reduce
import operator


tc = int(input())


for _ in range(tc):
    n = int(input())
    if n == 3:
        print("2 1 3")
        continue
    a = set()
    b = set()
    val = 2
    for i in range(n // 2):
        a.add(val)
        val += 1
        b.add(val)
        val += 1
    if n % 2 == 0:
        b.pop()
    while True:
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
        res_last = int("".join(last), 2)
        # print("".join(last), ax, bx, f"{(res_last):031b}")
        if (res_last in a) or (res_last in b):
            lst_b = b.pop()
            lst_b += 1
            while (lst_b in a) or (lst_b in b):
                lst_b += 1
            b.add(lst_b)
            continue
        if n % 2 == 0:
            b.add(res_last)
        else:
            a, b = b, a
            a.add(res_last)
        break
    # print(f"{n=}")
    # print(f"{a=} {b=}")
    # print("@", a_xor, b_xor ^ res_last)
    # print("@", reduce(operator.xor, a), reduce(operator.xor, b))
    while a or b:
        if a:
            print(a.pop(), end=" ")
        if b:
            print(b.pop(), end=" ")
    print()
