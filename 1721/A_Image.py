tc = int(input())

for _ in range(tc):
    a, b = list(input())
    c, d = list(input())
    st = set((a, b, c, d))
    print(len(st)-1)