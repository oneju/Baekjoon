# 두 용액
# https://www.acmicpc.net/problem/2470
import sys
input = sys.stdin.readline
N = int(input().strip())
lst = list(map(int, input().strip().split(" ")))
'''
배열 내
두 수의 합이
0 에 가까운 수를 만들어낼 경우
오름차순 출력
두 수의 합의 abs 가 가장 작은 경우아닐까?

'''
lst.sort(key = lambda x:abs(x))
ans = sys.maxsize

a=b=0
for i in range(len(lst)-1):
  if abs(lst[i]+lst[i+1]) < ans:
    a= min(lst[i],lst[i+1])
    b= max(lst[i],lst[i+1])
    ans = abs(a+b)
print(a,b)