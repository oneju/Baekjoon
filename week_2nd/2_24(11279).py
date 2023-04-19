# 최대 힙
# https://www.acmicpc.net/problem/11279
import sys
input = sys.stdin.readline
N = int(input())
heap = []
def heappush(num):
    heap.append(num)
    cur = len(heap)-1
    parent = (cur-1)//2
    
    while cur > 0:
        if heap[cur] > heap[parent]:
            # 현재 위치를 부모노드로 변경
            heap[cur], heap[parent] = heap[parent], heap[cur]
        cur = parent
        parent = (cur-1)//2

def heappop():
    heap[0] = heap[-1]
    heap.pop()
    cur = 0
    
    while True:
        left = 2*cur +1
        right = left +1
        idx = cur
        
        if left < len(heap) and heap[left] > heap[cur]:
            cur = left
        if right < len(heap) and heap[right] > heap[cur]:
            cur = right
        if idx!=cur: # cur 값이 바꼈다면,
            heap[idx], heap[cur] = heap[cur], heap[idx]
        else:
            break

for _ in range(N):
    com = int(input())
    
    if com == 0:
        if heap:
            print(heap[0])
            heappop()
        else:
            print(0)
    else:
        heappush(com)
