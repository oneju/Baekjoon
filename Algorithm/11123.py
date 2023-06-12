# 양 한마리... 양 두마리...
# https://www.acmicpc.net/problem/11123
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    h,w = map(int,input().split())
    f = [list(input()) for _ in range(h)]
    print(f)
    xi = [0,0,1,-1]
    yi = [1,-1,0,0]
    visit = [[0]*w for _ in range(h)]
    def find(x,y):
        stack = []
        stack.append([x,y])
        visit[x][y] = 1
        while stack:
            xx,yy = stack.pop()
            for a in range(4):
                if xx+xi[a] in range(h) and yy+yi[a] in range(w):
                    if visit[xx+xi[a]][yy+yi[a]] == 0 and f[xx+xi[a]][yy+yi[a]] == "#":
                        stack.append([xx+xi[a],yy+yi[a]])
                        visit[xx+xi[a]][yy+yi[a]] = 1

    cnt=0
    for i in range(h):
        for j in range(w):
            if visit[i][j] == 0 and f[i][j] == "#":
                find(i,j)
                cnt+=1
    print(cnt)