# 막대기
# https://www.acmicpc.net/problem/17608
import sys
N = int(sys.stdin.readline().strip())
lst = [int(sys.stdin.readline().strip()) for _ in range(N)]

pivot = lst[len(lst)-1]

cnt = 1
for i in range(N-2,-1,-1):
    if lst[i] > pivot:
        cnt +=1
        pivot = max(lst[i], pivot) 
print(cnt)