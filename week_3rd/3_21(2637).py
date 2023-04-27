# 장난감 조립
# https://www.acmicpc.net/problem/2637
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
m = int(input())
need = [[] for _ in range(n)]
indegree = [0] * n
for _ in range(m):
    x,y,k = map(int,input().split())
    need[y-1].append([x-1,k])
    indegree[x-1]+=1
# need = [[[4, 2]], [[4, 2]], [[5, 3]], [[5, 4], [6, 5]], [[6, 2], [5, 2]], [[6, 3]], []]       
# indegree = [0, 0, 0, 0, 2, 3, 3]
    
comp_list = [[0]*n for _ in range(n)]
def topolo():
    queue = deque()
    for i in range(n):
        if indegree[i] == 0:
            comp_list[i][i] = 1
            queue.append(i) # queue = [0,1,2,3]
    while queue:
        comp = queue.popleft() # comp = [0]
        for next, next_cnt in need[comp]:
            for i in range(n):
                comp_list[next][i] += comp_list[comp][i] * next_cnt
            indegree[next]-=1
            if indegree[next] == 0:queue.append(next)

topolo()
# comp_list = [ 5:[2, 2, 0, 0, 0, 0, 0], 6:[4, 4, 3, 4, 0, 0, 0], 7:[16, 16, 9, 17, 0, 0, 0]]
for i in range(n):
    if comp_list[n-1][i] != 0:
        print(i+1,comp_list[n-1][i])