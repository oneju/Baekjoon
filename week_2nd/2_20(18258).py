# 큐 2
# https://www.acmicpc.net/problem/18258
import sys
from collections import deque

input = sys.stdin.readline
N = int(input().strip())
queue = deque()

for _ in range(N):
    lst = input().strip().split()
    com = lst[0]
    if com == "push":
        queue.append(lst[1])
    elif com == "pop":
        if queue:
            print(queue[0])
            queue.popleft()
        else:
            print(-1)
    elif com == "size":
        print(len(queue))
    elif com == "empty":
        if not queue:
            print(1)
        else:
            print(0)
    elif com == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    else:
        if queue:
            print(queue[-1])
        else:
            print(-1)
        