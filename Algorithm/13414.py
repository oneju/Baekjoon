# 수강신청
# https://www.acmicpc.net/problem/13414
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
lec = {}
for i in range(m):
    lec[input().strip()] = i
lec = sorted(lec.items(), key = lambda x:x[1])
print()
for i in range(n):
    if i>=len(lec):break
    print(lec[i][0])