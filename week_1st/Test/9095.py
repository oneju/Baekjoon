# 1,2,3 더하기 - 재귀
import sys
T = int(sys.stdin.readline())

lst = [1,2,4]

def recur(n):
    if n <= 3:
        return lst[n-1]
    return recur(n-1) + recur(n-2) + recur(n-3)

for _ in range(T):
    n = int(sys.stdin.readline())
    print(recur(n))