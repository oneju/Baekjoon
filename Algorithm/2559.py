# 수열
# https://www.acmicpc.net/problem/2559
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
temp_lst = list(map(int,input().split()))
sum_lst = [0]*(n-m+1)
sum_lst[0] = sum(temp_lst[:m])
for i in range(1,len(sum_lst)):
    sum_lst[i] = sum_lst[i-1]-temp_lst[i-1]+temp_lst[i+m-1]
print(max(sum_lst))