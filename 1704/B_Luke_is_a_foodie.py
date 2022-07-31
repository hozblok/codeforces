tc = int(input())

for _i in range(tc):
    n, x = list(map(int, input().split()))
    a = list(map(int, input().split()))
    # prev_mode: Literal["lte"] | Literal["gt"] = "lte"
    # mode: Literal["lte"] | Literal["gt"] = "lte"
    # cur = 0
    mn = 0
    mx = 0
    count = 0
    for i, el in enumerate(a):
        if mn == 0:
            mn = el
            mx = el
        else:
            mn = min(el, mn)
            mx = max(el, mx)
            if mx - mn > 2 * x:
                count += 1
                mn = el
                mx = el
        # swp = False
        # if el <= x:
        #     if cur == 0:
        #         mode = "lte"
        #         cur = el + x
        #     elif mode != "lte":
        #         print("swp", mode, el, cur)
        #         swp = True
        #         res.append(cur)
        #         cur = el + x
        #         mode = "lte"
        #     else:
        #         swp = False
        # elif (el - cur) <= x:
        #     pass
        # else:
        #     if cur == 0:
        #         mode = "gt"
        #         cur = el - x
        #     elif mode != "gt":
        #         print("swp", mode, "-> gt",  el, cur)
        #         swp = True
        #         res.append(cur)
        #         cur = el - x
        #         mode = "gt"
        #     else:
        #         swp = False
        # if swp:
        #     swp = False
        # if mode == "lte":
        #     cur = min(cur, el + x)
        # elif mode == "gt":
        #     cur = max(cur, el - x)
    # if res and res[-1] != cur:
    #     res.append(cur)
    # print("@@@@", len(res), [*res, cur])
    print(count)
