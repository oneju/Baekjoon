#수 정렬하기
import sys
input = sys.stdin.readline
N = int(input())
lst = []
for i in range(N):
    lst.append(int(input()))
lst.sort()
[print(i) for i in lst]