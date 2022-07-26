tc = int(input())
for _ in range(tc):
    n = int(input())
    nums = list(map(int, (input()).split()))
    for i in range(n):
        v = ((input()).split())[1]
        for c in v:
            if c == "D":
                nums[i] += 1
            else:
                # 1 and 10 - wrong, cause 0 could be in nums from input
                if nums[i] == 0:
                    nums[i] = 9
                else:
                    nums[i] -= 1
    print(" ".join(map(lambda x: (str(x))[-1], nums)))
