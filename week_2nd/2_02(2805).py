# 나무 자르기
# https://www.acmicpc.net/problem/2805
import sys
N, M = map(int, sys.stdin.readline().strip().split(" "))
trees = list(map(int, sys.stdin.readline().strip().split(" ")))

pl = 1
pr = max(trees)

while pl <= pr:
    key = (pl+pr)//2
    K=0
    for tree in trees:
        if tree >= key:
            K+=(tree-key)
    if K >= M:
        pl = key+1
    else:
        pr = key-1
print(pr)
