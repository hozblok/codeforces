tc = int(input())

for _ in range(tc):
    word = input()
    et = "codeforces"
    count = 0
    for i, el in enumerate(word):
        if el != et[i]:
            count += 1
    print(count)
