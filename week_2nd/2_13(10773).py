# 제로
# https://www.acmicpc.net/problem/10773
import sys
input = sys.stdin.readline
K = int(input().strip())

lst = []
for i in range(K):
    mon = int(input().strip())
    
    if mon == 0:
        lst.pop()
    else:
        lst.append(mon)
print(sum(lst))