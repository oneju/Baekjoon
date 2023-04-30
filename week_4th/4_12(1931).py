# 회의실 배정
# https://www.acmicpc.net/problem/1931
N = int(input())
schedule = [list(map(int,input().split())) for _ in range(N)]
schedule.sort(key=lambda x:(x[1],x[0]))

cur = 0
cnt = 0
for conf in schedule:
    if conf[0] >= cur:
        cnt +=1
        cur = conf[1]
print(cnt)