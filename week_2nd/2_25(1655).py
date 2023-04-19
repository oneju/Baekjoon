# 가운데를 말해요
# https://www.acmicpc.net/problem/1655
import sys
from heapq import heappush, heappop

input = sys.stdin.readline
N = int(input())
min_heap = [] # 최대힙으로
max_heap = [] # 최소힙으로

'''
수를 받아서, 두 힙의 크기가 같으면, min_heap 에 push
아니면 max_heap 에 push
max_heap과 min_heap 의 [0] 값을 비교
max_heap[0]값이 더 작으면, 바꾸기
'''
# min = [-1] max = [5]
for _ in range(N):
    num = int(input()) # num = 2
    
    if len(min_heap) == len(max_heap):
        heappush(min_heap,-num) # min = [-2,-1]
    else:
        heappush(max_heap,num)
        
    if max_heap and -min_heap[0] > max_heap[0]: # min[0] = -(-2) max[0] = 5
        a,b= heappop(min_heap), heappop(max_heap) # heappop
        
        # 음수로 받았기 때문에 양수로 변환, min은 반대
        heappush(max_heap, -a) 
        heappush(min_heap, -b) 

    print(-min_heap[0])