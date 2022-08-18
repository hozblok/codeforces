tc = int(input())

def maxs(numbers):
    m1 = m2 = (-1, float('-inf'))
    for i, x in enumerate(numbers):
        if x > m2[1]:
            if x >= m1[1]:
                m1, m2 = (i, x), m1
            else:
                m2 = (i, x)
    return m1, m2

def mins(numbers):
    m1 = m2 = (-1, float('+inf'))
    for i, x in enumerate(numbers):
        if x < m2[1]:
            if x <= m1[1]:
                m1, m2 = (i, x), m1
            else:
                m2 = (i, x)
    return m1, m2

for  _ in range(tc):
    n = int(input())
    ar = list(map(int, input().split()))
    m1, m2 = maxs(ar)
    n1, n2 = mins(ar)
    print(m1[1] + m2[1] - n1[1] -n2[1])