tc = int(input())

for _ in range(tc):
    n = input()
    word = map(int, input().split())
    mx = 0
    count = 0
    for i, c in enumerate(word):
        if c == 1:
            if mx < count:
                mx = count
            count = 0
        elif c == 0:
            count += 1
    if mx < count:
        mx = count
        count = 0
    print(mx)
