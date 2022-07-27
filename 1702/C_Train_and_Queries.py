tc = int(input())

for _ in range(tc):
    input()
    l, lq = list(map(int, input().split()))
    route = input().split()
    dct = {}
    for i, el in enumerate(route):
        if el not in dct:
            dct[el] = (i, i)
        if el in dct:
            dct[el] = (dct[el][0], i)
    for __ in range(lq):
        a, b = input().split()
        if a in dct and b in dct:
            if dct[a][0] < dct[b][1]:
                print("yes")
            else:
                print("no")
        else:
            print("no")
