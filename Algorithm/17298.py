# 오큰수
# https://www.acmicpc.net/problem/17298
import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
ans = [-1] * n
stack = []
for i in range(n-1,-1,-1):
    while stack:
        if stack[-1] > arr[i]:
            ans[i] = stack[-1]
            break
        stack.pop()
    stack.append(arr[i])
print(*ans)