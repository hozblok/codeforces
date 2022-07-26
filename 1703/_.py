arr = [[0, 1, 1, 0], [0, 0, 0, 1], [0, 1, 1, 0], [0, 1, 0, 0]]

l = len(arr)
for i in range(l):
    for j in range(l):
        print(arr[i][j], end=" ")
    print()

print("######90 deg######")
for i in range(l):
    for j in range(l):
        print(arr[l - j - 1][i], end=" ")
    print()

print("#####180 deg######")
for i in range(l):
    for j in range(l):
        print(arr[l - i - 1][l - j - 1], end=" ")
    print()

print("#####270 deg######")
for i in range(l):
    for j in range(l):
        print(arr[j][l - i - 1], end=" ")
    print()
