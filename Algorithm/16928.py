# 뱀과 사다리 게임
# https://www.acmicpc.net/problem/16928
import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
board = [i for i in range(101)]
count = [0] * 101
for _ in range(n+m):
    x,y = map(int,input().split())
    board[x] = y

def game():
    queue = deque()
    queue.append(1)
    while queue:
        visit = queue.popleft()
        for i in range(1,7):
            next = board[visit+i]
            if count[next] == 0:
                queue.append(next)
                count[next] = count[board[visit]]+1
            if next == 100:
                return count[visit]+1

print(game())