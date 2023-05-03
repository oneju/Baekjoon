import sys
input = sys.stdin.readline

n,m = map(int,input().split())
n_lst = list(map(int,input().split()))
S_lst = [0]*(n+1)
C = [0] * m
for i in range(1,n+1):
    S_lst[i] =S_lst[i-1]+n_lst[i-1]
    C[S_lst[i]%m]+=1
cnt = C[0]
for i in range(m):
    cnt += (C[i] * (C[i]-1) // 2)
print(cnt)