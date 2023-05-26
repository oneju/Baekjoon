# 기타줄
# https://www.acmicpc.net/problem/1049
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
se = si = 1000
price = 1000*20
for _ in range(m):
    e,i = map(int,input().split())
    se = min(se,e)
    si = min(si,i)
price_s = (se*(n//6)) + (si*(n%6))
price = min(price,price_s,si*n,se*((n//6)+1))
print(price)