# 연산자 끼워넣기
# https://www.acmicpc.net/problem/14888
import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int,input().split())) # 숫자
pl,mi,mu,di = map(int,input().split()) # +, -, *, /
mini = sys.maxsize
maxi = -sys.maxsize

def dfs(i,cal):
    global pl,mi,mu,di,mini,maxi
    
    if i == N-1:
        mini = min(mini,cal)
        maxi = max(maxi,cal)
        
    if pl>0:
        pl-=1
        dfs(i+1,cal+A[i+1])
        pl+=1
    if mi>0:
        mi-=1
        dfs(i+1,cal-A[i+1])
        mi+=1
    if mu>0:
        mu-=1
        dfs(i+1,cal*A[i+1])
        mu+=1
    if di>0:
        di-=1
        dfs(i+1,int(cal/A[i+1]))
        di+=1
        
dfs(0,A[0])
print(maxi)
print(mini)