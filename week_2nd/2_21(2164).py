# 카드 2
# https://www.acmicpc.net/problem/2164
import sys
from collections import deque

input = sys.stdin.readline
N = int(input().strip())
queue = deque()
for i in range(N):queue.append(i+1)

while len(queue) > 1:
    queue.popleft()
    a = queue.popleft()
    queue.append(a)
print(queue[0])