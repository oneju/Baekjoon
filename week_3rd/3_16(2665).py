# 미로 만들기
# https://www.acmicpc.net/problem/2665
import sys
import heapq
input = sys.stdin.readline
n = int(input())
rooms = [input() for _ in range(n)]

# 이동할 방향 (↓ → ↑ ←)
x_info = [0, -1, 0, 1]
y_info = [1, 0, -1, 0]
def dijkstra():
    miro = [[float('INF')] * n for _ in range(n)]
    heap = []
    heapq.heappush(heap, (0,0,0)) # cost, x, y
    miro[0][0] = 0
    while heap:
        cost,x,y = heapq.heappop(heap)
        
        for i in range(4):
            xx = x+x_info[i]
            yy = y+y_info[i]
            if xx in range(n) and yy in range(n) and miro[xx][yy] == float('INF'):
                if rooms[xx][yy] == '1':
                    miro[xx][yy] = cost
                    heapq.heappush(heap, (cost, xx, yy))
                else:
                    miro[xx][yy] = cost+1
                    heapq.heappush(heap,(cost+1, xx, yy))
    return miro

miro = dijkstra()
print(miro[n-1][n-1])