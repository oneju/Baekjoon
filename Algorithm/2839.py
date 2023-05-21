# 설탕 배달
# https://www.acmicpc.net/problem/2839
import sys
input = sys.stdin.readline
n = int(input())
cnt = n//5
n%=5
while n>=0:
    if n%3==0:
        cnt+=n//3
        break
    cnt-=1
    n+=5
    if cnt<0:
        cnt = -1
        break
print(cnt)