from collections import defaultdict


tc = int(input())

for _ in range(tc):
    res = True
    n = int(input())
    s1 = set()
    s2 = set()
    s = defaultdict(list)
    arr = []
    for dom in range(n):
        x, y = input().split()
        arr.append((int(x), int(y)))
    arr.sort()
    for a, b in arr:
        if a == b:
            res = False
            break
        s[a].append(b)
        s[b].append(a)
        if len(s[a]) > 2 or len(s[b]) > 2:
            res = False
            break
        if a in s1 or b in s1:
            if a in s2 or b in s2:
                res = False
                break
            else:
                s2.add(a)
                s2.add(b)
        else:
            s1.add(a)
            s1.add(b)
    print("YES" if res else "NO")
