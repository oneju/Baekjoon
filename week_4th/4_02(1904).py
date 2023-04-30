# 01타일
# https://www.acmicpc.net/problem/1904
import sys
input = sys.stdin.readline
n = int(input())
'''
memo = [0] * (n+1)

def TopDOWN(n):
    if n<=2:return n
    if memo[n]!=0:return memo[n] % 15746
    memo[n] = TopDOWN(n-1) + TopDOWN(n-2)
    return memo[n] % 15746

print(TopDOWN(n))

'''
prev = cur = 1
for i in range(2,n+1):
    res = (prev + cur) % 15746
    prev = cur
    cur = res
print(cur)