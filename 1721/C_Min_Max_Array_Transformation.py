tc = int(input())


def binary_search(arr, x, gt=True):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
        # means x is present at mid
        else:
            break

    if gt:
        res = mid if arr[mid] >= x else mid + 1
        res = res if res < len(arr) else res - 1
    else:
        res = mid if arr[mid] <= x else mid - 1
        # res = res if res >= 0  else 0
    return res


for _ in range(tc):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    mn = b[0]
    d_min = []
    d_max = []
    for i, el_a in enumerate(a):
        mid1 = binary_search(b, el_a, gt=True)
        d_min.append(b[mid1] - el_a)
        mid2 = binary_search(a, b[i], gt=False)
        # print("@", b[mid2 if mid2 >= 0 else 0], el_a, end=" ")
        d_max.append(max(b[mid2] - el_a, 0))
    # print()
    print(" ".join(map(str, d_min)))
    print(" ".join(map(str, d_max)))