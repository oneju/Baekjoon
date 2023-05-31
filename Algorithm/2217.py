# 로프
# https://www.acmicpc.net/problem/2217
import sys
input = sys.stdin.readline
n = int(input())
rope = []
for _ in range(n):
    rope.append(int(input()))
rope.sort()
ans = 0
for i in range(n):
    ans = max(ans,rope[i]*(n-i))
print(ans)