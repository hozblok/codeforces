tc = int(input())

for el in range(tc):
    n = int(input())
    print(n - 10 ** (len(str(n)) - 1))
