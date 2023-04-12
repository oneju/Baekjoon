# 수정렬하기 3
import sys
input = sys.stdin.readline
N = int(input())

lst = [0]*10001

for i in range(N):
    lst[int(input())]+=1

for idx in range(10001):
    if lst[idx] ==0:
        idx+=1
    else:
        while lst[idx]>0:
            print(idx)
            lst[idx]-=1
