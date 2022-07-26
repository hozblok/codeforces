from collections import defaultdict


tc = int(input())
m = {
    2: [(1, 1)],
    3: [(1, 2), (2, 1)],
    4: [(1, 3), (2, 2), (3, 1)],
    5: [(1, 4), (2, 3), (3, 2), (4, 1)],
    6: [(1, 5), (2, 4), (3, 3), (4, 2), (5, 1)],
    7: [(1, 6), (2, 5), (3, 4), (4, 3), (5, 2), (6, 1)],
    8: [(1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2), (7, 1)],
}
for _ in range(tc):
    result = []
    num_s = int(input())
    d = defaultdict(set)
    ss = []
    for _ in range(num_s):
        s = input()
        d[len(s)].add(s)
        ss.append(s)
    for s in ss:
        if len(s) <= 1:
            result.append(0)
        else:
            res = False
            for l_len, r_len in m[len(s)]:
                res = res or (s[:l_len] in d[l_len] and s[l_len:] in d[r_len])
                if res:
                    break
            result.append(int(res))
    print("".join(map(str, result)))
