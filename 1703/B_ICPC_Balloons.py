n = int(input())
for i in range(n):
    l, inp = int(input()), input()
    s = set()
    count = 0
    for c in inp:

        if c in s:
            count += 1
        else:
            count += 2
            s.add(c)
    print(count)
