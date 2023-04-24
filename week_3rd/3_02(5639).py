# 이진 검색 트리
# https://www.acmicpc.net/problem/5639
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
lst = []
while True:
    try:
        lst.append(int(input()))
    except: # 오류가 생기면 종료(예외)
        break
    
def recur(s,e):
    if s == e:
        print(lst[s])
        return
    mid = s
    root = lst[s]
    for a in range(s+1,e+1):
        if lst[a] > root:
            mid = a
            break
    if mid in [s,s+1]: # 왼쪽이나 오른쪽이 없다면
        recur(s+1,e)
    else:
        recur(s+1,mid-1) # 왼쪽 범위
        recur(mid,e) # 오른쪽 범위
    print(root)
    return

recur(0,len(lst)-1)