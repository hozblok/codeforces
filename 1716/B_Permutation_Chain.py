tc = int(input())

for _ in range(tc):
    n = int(input())
    a = [el  for el in range(1, n+1)]
    print(n)
    print(" ".join(map(str, a)))
    for i in range(n-1):
        j = i + 1
        a[i], a[j] = a[j], a[i]
        print(" ".join(map(str, a)))