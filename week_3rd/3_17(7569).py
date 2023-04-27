# 토마토
# https://www.acmicpc.net/problem/7569
import sys
from collections import deque
input = sys.stdin.readline
m,n,h = map(int,input().split())
box = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]

'''
1:익은 토마토
0:익지않은 토마토
-1:없는 토마토
'''

x_info = [1, 0, -1, 0, 0, 0] # []
y_info = [0, -1, 0, 1, 0, 0] # [][]
z_info = [0, 0, 0, 0, -1, 1] # [][][]

def bfs():
    queue = deque()
    for z in range(h):
        for i in range(n):
            for j in range(m):
                if box[z][i][j] == 1:
                    queue.append([z,i,j])

    while queue:
        z,x,y = queue.popleft()
        
        for i in range(6):
            zz = z + z_info[i]
            xx = x + x_info[i]
            yy = y + y_info[i]
            if zz in range(h) and xx in range(n) and yy in range(m):
                if box[zz][xx][yy] == 0:
                    box[zz][xx][yy] = box[z][x][y] + 1
                    queue.append([zz,xx,yy])

bfs()
day = 0
for i in box:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
        day = max(day,max(j))
print(day-1)