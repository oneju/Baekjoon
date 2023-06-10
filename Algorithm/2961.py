# 도영이가 만든 맛있는 음식
# https://www.acmicpc.net/problem/2961
import sys
input = sys.stdin.readline
N = int(input())
food = [list(map(int,input().split()))for _ in range(N)]

def cooking(cook):
    sour = 1
    bitter = 0
    for i in range(N):
        if 1<<i & cook == 1<<i:
            sour*=food[i][0]
            bitter+=food[i][1]
    return abs(sour-bitter)

ans = sys.maxsize
for i in range(1,1<<N):
    ans = min(ans,cooking(i))
print(ans)