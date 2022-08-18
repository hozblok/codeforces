tc = int(input())

rr = {0, 1, 2, 4, 8, 16, 32, 64, 128}

# TODO
for _ in range(tc):
    n = int(input())
    ar = list(map(int, input().split()))

    print(sum(1 for el in ar if el in rr))
