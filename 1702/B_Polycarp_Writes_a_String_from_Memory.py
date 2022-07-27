tc = int(input())

for _ in range(tc):
    s = input()
    st = set()
    count = 1
    for el in s:
        if len(st) == 3 and el not in st:
            count += 1
            st.clear()
        st.add(el)
    print(count)
