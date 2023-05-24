# 수열
# https://www.acmicpc.net/problem/2559
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
temp_lst = list(map(int,input().split()))
temp_sum = MAX = sum(temp_lst[:m])
for i in range(1,n-m+1):
    temp_sum  = temp_sum - temp_lst[i-1] + temp_lst[i+m-1]
    if MAX < temp_sum:
        MAX = temp_sum
print(MAX)