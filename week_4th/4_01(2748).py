# 피보나치 수 2
# https://www.acmicpc.net/problem/2748
import sys
input = sys.stdin.readline
n = int(input())

def BottomUP():
    tab = [0] * (n+1)
    tab[1] = 1
    for i in range(2,n+1):
        tab[i] = tab[i-1] + tab[i-2]
    return tab[n]

def TopDOWN(n):
    memo = [0] * (n+1)
    if n<=1:return n
    if memo[n]!=0:return memo[n]
    memo[n] = TopDOWN(n-1) + TopDOWN(n-2)
    return memo[n]

print(BottomUP())
print(TopDOWN(n))