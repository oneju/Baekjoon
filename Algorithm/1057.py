# 토너먼트
# https://www.acmicpc.net/problem/1057
n,k,l = map(int,input().split())
round = 0
while k!=l:
    k = k//2+k%2
    l = l//2+l%2
    round+=1
print(round)