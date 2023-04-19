# 카드 정렬하기
# https://www.acmicpc.net/problem/1715
import sys
from heapq import heappush, heappop
input = sys.stdin.readline
N = int(input())
'''
10 20 40
-> 10+20 + (10+20)+40 = 100
'''
cards = []
for _ in range(N):
    heappush(cards,int(input()))
    # cards 를 최소힙으로 구성하여 push
    
val = 0
sum = 0
for i in range(1,N):
    val = heappop(cards)+heappop(cards)
    heappush(cards, val)
    # 앞에서 부터 더한 값 저장
    sum+=val
print(sum)