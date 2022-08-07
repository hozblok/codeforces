from tkinter import S


tc = int(input())

for _ in range(tc):
    n = int(input())
    #  () -> 1, (()) -> 2, ((())) -> 3
    # () () () () 1 1 1 1
    # (()) () ()  2 1 1
    # () (()) ()  1 2 1
    # () () (())  1 1 2
    #
    print("()" * n)
    for i in range(n - 1):
        print("".join("()" if el != i else "(())" for el in range(n)))
