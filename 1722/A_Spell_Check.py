tc = int(input())

for _ in range(tc):
    n = int(input())
    s = input()
    if n != 5:
        print("NO")
    else:
        ss = set(s)
        if all(t in ss for t in "Timur"):
            print("YES")
        else:
            print("NO")
