# 요세푸스 문제 0
# https://www.acmicpc.net/problem/11866
import sys

input = sys.stdin.readline
N, K = map(int,input().strip().split(" "))
lst = [i+1 for i in range(N)]
joseph = []
idx = 0
while lst:
    idx = (idx+K-1) % len(lst)
    num = lst.pop(idx)
    joseph.append(num)
print("<",end="")
[print(joseph[i],end=", ") for i in range(len(joseph)-1)]
print(f"{joseph[-1]}>")