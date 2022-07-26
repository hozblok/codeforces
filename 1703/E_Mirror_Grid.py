ntc = int(input())
for el in range(ntc):
    l = int(input())
    ar = []
    for i in range(l):
        ar.append(list(map(int, input())))

    count = 0
    for i in range(l):
        for j in range(l):
            same = [
                ar[i][j],
                ar[l - j - 1][i],
                ar[l - i - 1][l - j - 1],
                ar[j][l - i - 1],
            ]
            a0 = sum(1 for el in same if el == 0)
            if a0 == 0 or a0 == 4:
                continue
            elif a0 == 1 or a0 == 3:
                count += 1
            else:
                count += 2
    print(count // 4)
