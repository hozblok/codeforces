tc = int(input())

ps = {'G', 'B'}

for _ in range(tc):
    n = int(input())
    s1 = input()
    s2 = input()
    res = True
    for i, c1 in enumerate(s1):
        c2 = s2[i]
        if c2 == c1 or (c1 in ps and c2 in ps):
            continue
        else:
            res = False
            break
    print("YES" if res else "NO")