# 수들의 합 5
# https://www.acmicpc.net/problem/2018
import sys
N = int(sys.stdin.readline())
i = j = num = cnt = 1
while i<N:
    if num == N:
        cnt+=1
        num-=i
        i+=1
    elif num > N:
        num-=i
        i+=1
    else:
        j+=1
        num+=j
print(cnt)