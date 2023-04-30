# 최소비용 구하기
# https://www.acmicpc.net/problem/1916
import sys
import heapq
input = sys.stdin.readline
N = int(input()) # 도시 수
M = int(input()) # 버스 수
# 버스 노선 from to cost M개
bus = [[]for _ in range(N)]
for _ in range(M):
    a,b,c = map(int,input().split())
    bus[a-1].append([c,b-1])
start, end = map(int,input().split())

def dijkstra(start,end):
    # initialize
    graph = [float('INF')] * N
    graph[start] = 0
    heap = []
    heapq.heappush(heap,(graph[start], start))
    while heap:
        cost, city = heapq.heappop(heap)
        if graph[city] >= cost:
            for next in bus[city]:
                if graph[next[1]] > next[0] + cost:
                    graph[next[1]] = next[0] + cost
                    heapq.heappush(heap,(graph[next[1]],next[1]))
    return graph

graph = dijkstra(start-1,end-1)
print(graph[end-1])