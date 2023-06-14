# 적록색약
# https://www.acmicpc.net/problem/10026
import sys
input = sys.stdin.readline
N = int(input())
color_lst = [list(input())for _ in range(N)]
def dfs(x,y,c):
    if color_lst[x][y] in ['R','G']:
        color_lst[x][y] = 'A'
    visit[x][y] = 1
    xi = [0,0,1,-1]
    yi = [-1,1,0,0]
    no = 0
    for i in range(4):
        if x+xi[i] in range(N) and y+yi[i] in range(N):
            if color_lst[x+xi[i]][y+yi[i]] == c and visit[x+xi[i]][y+yi[i]]==0:
                dfs(x+xi[i],y+yi[i],c)
                no = 1
    if no==0:return
cnt_a = cnt_b = 0
visit = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0:
            dfs(i,j,color_lst[i][j])
            cnt_a += 1

visit = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if visit[i][j] == 0:
            dfs(i,j,color_lst[i][j])
            cnt_b += 1
print(cnt_a,cnt_b)