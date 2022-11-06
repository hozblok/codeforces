import os, sys
from io import BytesIO, IOBase

from collections import Counter

# # Fast IO Region
# BUFSIZE = 8192


# class FastIO(IOBase):
#     newlines = 0

#     def __init__(self, file):
#         self._fd = file.fileno()
#         self.buffer = BytesIO()
#         self.writable = "x" in file.mode or "r" not in file.mode
#         self.write = self.buffer.write if self.writable else None

#     def read(self):
#         while True:
#             b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
#             if not b:
#                 break
#             ptr = self.buffer.tell()
#             self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
#         self.newlines = 0
#         return self.buffer.read()

#     def readline(self):
#         while self.newlines == 0:
#             b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
#             self.newlines = b.count(b"\n") + (not b)
#             ptr = self.buffer.tell()
#             self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
#         self.newlines -= 1
#         return self.buffer.readline()

#     def flush(self):
#         if self.writable:
#             os.write(self._fd, self.buffer.getvalue())
#             self.buffer.truncate(0), self.buffer.seek(0)


# class IOWrapper(IOBase):
#     def __init__(self, file):
#         self.buffer = FastIO(file)
#         self.flush = self.buffer.flush
#         self.writable = self.buffer.writable
#         self.write = lambda s: self.buffer.write(s.encode("ascii"))
#         self.read = lambda: self.buffer.read().decode("ascii")
#         self.readline = lambda: self.buffer.readline().decode("ascii")


# sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
# input = lambda: sys.stdin.readline().rstrip("\r\n")

T = int(input())

for _ in range(T):
    n = int(input())
    s = input()

    if n == 1:
        print(1)
    elif n == 2:
        if s[0] == s[1]:
            print(4)
        else:
            print(1)
    elif n == 3:
        if s[1] == s[0] == s[2]:
            print(9)
        elif s[1] == s[0] or s[1] == s[2]:
            print(4)
        else:
            print(2)
    else:
        cnt = 1
        cnt_cur = 1
        prev = s[0]
        for i in range(1, n):
            if s[i] == prev:
                cnt_cur += 1
            else:
                cnt = max(cnt_cur, cnt)
                cnt_cur = 1
                prev = s[i]
        cnt = max(cnt_cur, cnt)
        # start = n // 2
        # if n % 2 == 1:
        #     start += 1
        # ok = s[start]
        # ok1, ok2 = ok, ok
        # d[ok] += 1
        # count = 1
        # i = 1
        # while True:
        #     nxt1, nxt2 = start - i, start + i
        #     i += 1
        #     if nxt1 >= 0:
        #         d[s[nxt1]] += 1
        #         print('->',s[nxt1], ok1)
        #         if s[nxt1] == ok1:
        #             count += 1
        #         else:
        #             ok1 = None
        #     if nxt2 < len(s):
        #         d[s[nxt2]] += 1
        #         if s[nxt2] == ok2:
        #             count += 1
        #         else:
        #             ok2 = None
        #     if nxt1 < 0 and nxt2 >= len(s):
        #         break
        # res1 = cnt * cnt
        # res2 = d['0'] * d['1']
        # n2 = n // 2
        # if n % 2 == 1:
        # n2 += 1
        # print(s, n2, cnt, s.count('1'), n - s.count('1'))
        c = Counter(s)
        print(max(cnt**2, c["0"] * c["1"]))
