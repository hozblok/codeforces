tc = int(input())

for _ in range(tc):
    n = int(input())
    a = list(map(int, input().split()))
    prev = -1
    rep = set()
    res = []
    for i, el in enumerate(a):
        if el in rep or (res and el < res[-1]):
            while res:
                # print("@@", el, res[-1], el < res[-1])
                rep.add(res.pop())
                # print("@@@", rep)
        res.append(el)
        # print("@", res)
    print(len(rep))