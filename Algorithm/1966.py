# 프린터 큐
# https://www.acmicpc.net/problem/1966
import sys
from collections import deque
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    priority = list(map(int,input().split()))
    queue = deque(i for i in range(n))
    printing = 0
    while queue:
        idx = queue.popleft()
        a = 0
        for x in queue:
            if priority[idx] < priority[x]:
                a=1
                break
        if a==0:
            printing+=1
            if idx == m:
                print(printing)
                break
        else:queue.append(idx)