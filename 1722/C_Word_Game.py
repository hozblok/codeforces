from collections import defaultdict


tc = int(input())

for _ in range(tc):
    n = int(input())
    s1 = input().split()
    s2 = input().split()
    s3 = input().split()
    ss = defaultdict(int)
    for el in (*s1, *s2, *s3):
        ss[el] += 1
    res = [0, 0, 0]
    for i, s in enumerate((s1, s2, s3)):
        for word in s:
            res[i] += 0 if ss[word] == 3 else 1 if ss[word] == 2 else 3
    print(" ".join(map(str, res)))
