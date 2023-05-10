# 최솟값 찾기
# https://www.acmicpc.net/problem/11003
import sys
from collections import deque
input = sys.stdin.readline
N, L = map(int, input().split())
A = list(map(int,input().split()))

mini = deque()
D = []
for i in range(N):
    if A[mini[0]] <= A[i]: 
        if i - mini[0] < L:
            D.append(A[mini[0]])
        else:mini.popleft()
    else:mini.popleft()
    mini.append(i)
print(D)
    
    