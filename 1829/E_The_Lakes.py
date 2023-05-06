tc = int(input())

for _ in range(tc):
    n_, m_ = input().split()
    n, m = int(n_), int(m_)
    a = []
    touched = dict()
    res = 0
    for i in range(n):
        a.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(m):
            if touched.get((i, j), False):
                continue
            count = 0
            w = [(i, j)]
            while w:
                # print('@', w)
                x, y = w.pop()
                if touched.get((x, y), False):
                    continue
                if x < 0 or x >= n:
                    continue
                elif y < 0 or y >= m:
                    continue
                touched[(x, y)] = True
                if a[x][y] == 0:
                    continue
                else:
                    count += a[x][y]
                    for ii, jj in ((x-1, y), (x, y - 1), (x + 1, y), (x, y + 1)):
                        if ii < 0 or jj < 0:
                            continue
                        if ii >= n or jj >= m:
                            continue
                        w.append((ii, jj))
            if count > res:
                res = count
    print(res)
