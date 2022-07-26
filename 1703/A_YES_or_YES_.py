n = input()
for el in range(int(n)):
    var = input()
    if len(var) != 3:
        print("No")
    else:
        if var[0] in ("Y", "y") and var[1] in ("E", "e") and var[2] in ("S", "s"):
            print("Yes")
        else:
            print("No")
