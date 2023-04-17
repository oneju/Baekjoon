# 탑
# https://www.acmicpc.net/problem/2493
import sys
input = sys.stdin.readline
N = int(input().strip())
arr = list(map(int, input().strip().split(" ")))

lst = [0] * N
stk = []

for i in range(1,N):
    while stk:
        if arr[stk[-1]] > arr[i]:
            lst[i] = stk[-1] + 1
            break
        else:
            stk.pop()
    stk.append(i)

[print(num, end=" ") for num in lst]