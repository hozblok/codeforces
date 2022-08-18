import enum


tc = int(input())


for _ in range(tc):
    n, m = list(map(int, input().split()))
    a = []
    for i in range(n):
        a.append(list(map(int, input())))

    def gt(i: int, j: int):
        if i < 0 or j < 0:
            return None
        try:
            res = a[i][j]
            # print("#", i, j, res)
            return res
        except:
            return None

    count = 0
    zero_exists = False
    for i, row in enumerate(a):
        for j, el in enumerate(row):
            if el == 1:
                count += 1
            else:
                zero_exists = True
    two_zero = False
    for i, row in enumerate(a):
        if two_zero:
            break
        for j, el in enumerate(row):
            if el == 0:
                if any(
                    item == 0
                    for item in filter(
                        lambda x: x is not None,
                        map(
                            lambda x: gt(x[0], x[1]),
                            (
                                (i - 1, j),
                                (i + 1, j),
                                (i, j + 1),
                                (i, j - 1),
                                (i + 1, j + 1),
                                (i - 1, j - 1),
                                (i + 1, j - 1),
                                (i - 1, j + 1),
                            ),
                        ),
                    )
                ):
                    two_zero = True
                    break
    # print("@@", two_zero)
    if two_zero:
        print(count)
    elif zero_exists:
        print(count - 1)
    else:
        print(count - 2)
