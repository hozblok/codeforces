tc = int(input())

for _ in range(tc):
    n = int(input())
    a = list(map(int, input().split()))
    sm = None
    cnt = 0
    for el in a:
        if sm == None:
            sm = 0
        elif sm == 0:
            cnt += 1
        if el == 0:
            el = -sm
        sm += el
    if sm == 0:
        cnt += 1
    print(cnt)