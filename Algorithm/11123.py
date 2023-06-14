# 양 한마리... 양 두마리...
# https://www.acmicpc.net/problem/11123
import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
T = int(input())

xi = [0,0,1,-1]
yi = [1,-1,0,0]
# stack + while loop
def find_s(x,y):
    stack = []
    stack.append([x,y])
    f[x][y] = '.'
    while stack:
        xx,yy = stack.pop()
        for a in range(4):
            if xx+xi[a] in range(h) and yy+yi[a] in range(w):
                if f[xx+xi[a]][yy+yi[a]] == "#":
                    stack.append([xx+xi[a],yy+yi[a]])
                    f[xx+xi[a]][yy+yi[a]] = '.'
# recursion (error -> set limit)
def find_r(x,y):
    f[x][y] = "."
    no = 0
    for a in range(4):
        if x+xi[a] in range(h) and y+yi[a] in range(w):
            if f[x+xi[a]][y+yi[a]] == "#":
                find_r(x+xi[a],y+yi[a])
                no = 1
    if no == 0: return

for _ in range(T):
    h,w = map(int,input().split())
    f = [list(input()) for _ in range(h)]
    cnt=0
    for i in range(h):
        for j in range(w):
            if f[i][j] == "#":
                cnt+=1
                find_r(i,j)
    print(cnt)