# 점프
# https://www.acmicpc.net/problem/2253

# https://velog.io/@stkang9409/%EB%B0%B1%EC%A4%80-%EC%A0%90%ED%94%84-%EC%89%BD%EA%B2%8C-%EB%82%98%EC%98%A8-%ED%92%80%EC%9D%B4

import sys
input = sys.stdin.readline
n,m = map(int,input().split())
dp = [[sys.maxsize] * (int((2*n)**0.5)+2) for _ in range(n+1)]
small = [int(input()) for _ in range(m)]
dp[1][0] = 0
def jump():
    # dp[i][j] = i번째 돌에 j 속도로 도착했을 때의 이동 횟수
    for i in range(2,n+1):
        if i in small:continue
        # 속도를 올려가면서 이전 위치(현위치-속도)에서 세 값들 중 적은 값+1을 저장
        # (2*i)**0.5 = 최대 속도 = 현위치의 등차수열 합
        for j in range(1,int((2*i)**0.5)+1):
            dp[i][j] = min(dp[i-j][j-1],dp[i-j][j],dp[i-j][j+1])+1
    return min(dp[n])

ans = jump()
if ans == sys.maxsize:print(-1)
else:print(ans)