# TODO


tc = int(input())



def cnt(cl):
    it = iter(cl)
    next(it, None)
    count = 0
    while True:
        nx = next(it, None)
        if nx is None:
            break
        else:
            count += 1
        if nx >= count:
            count = nx + 1
    return count

for _ in range(tc):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c0 = []
    k = 0
    for k in range(2*n):
        reverse = False
        for j in range(n):
            if not reverse:
                for cl in (a, b):
                    c0.append(cl[j])
            else:
                for cl in (b, a):
                    c0.append(cl[j])
            reverse = not reverse

    c2 = []
    for cl in (a, list(reversed(b))):
        for j in range(n):
            c2.append(cl[j])

    c1 = []
    c1.append(a[0])
    a.reverse()
    for cl in (b, a):
        for el in cl:
            c1.append(el)
    c1.pop()
    print(c0, c1, c2)
    
    print(min(cnt(c0), cnt(c1), cnt(c2)))
    