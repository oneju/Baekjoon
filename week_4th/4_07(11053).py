# 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053
import sys
input = sys.stdin.readline
N = int(input())
arr = list(map(int,input().split()))

lst = [0]*N
lst[0] = 1

for i in range(1,N):
    num = 0
    for j in range(i):
        if arr[i] > arr[j] and num < lst[j]:
            num = lst[j]
    lst[i] = num+1
    
print(max(lst))