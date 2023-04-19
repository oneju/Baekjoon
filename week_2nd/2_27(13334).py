# 철로
# https://www.acmicpc.net/problem/13334
import sys
from heapq import heappop, heappush

input = sys.stdin.readline
n = int(input())
locations = []
for _ in range(n):
    i = list(map(int, input().split(" ")))
    i.sort()
    locations.append(i)
d = int(input())
'''
n = 사람 수
h, o = 집, 사무실의 위치
d = 철로의 길이

철로를 사용할 수 있는 최대 인원
https://yongjoonseo.dev/problem%20solving/python/PS-baekjoon037/
'''

heap = []
max_len = 0
# 철로의 시작점을 가장 작은 것부터 시작할 수 있도록 큰 원소를 기준으로 오름차순 정렬
locations.sort(key=lambda x:x[1])

for road in locations:
    # 집에서 회사 거리가 d보다 작을 때 push
    limit = road[1] - d
    if road[0]>=limit:
        heappush(heap, road)
    # limit = 시작점
    # limit 보다 작다는 것 = 시작점 바깥에 있다는 것
    while heap and heap[0][0]<limit:
        heappop(heap)
        
    # heap 의 최대 길이 저장    
    max_len = max(max_len, len(heap))
print(max_len)