# 가장 긴 증가하는 부분 수열
# https://www.acmicpc.net/problem/11053

import sys
input = sys.stdin.readline
N = int(input().strip())
A = list(map(int, input().strip().split(" ")))

# https://namu.wiki/w/%EC%B5%9C%EC%9E%A5%20%EC%A6%9D%EA%B0%80%20%EB%B6%80%EB%B6%84%20%EC%88%98%EC%97%B4

A = [0] + A

def LIS() :
  d = [0]
    
  for i in range(1, len(A)) :
    if d[-1] < A[i]:
      d.append(A[i])
    else :
      min, max = 0, len(d)-1
      save = 0
      while min <= max:
        mid = (min+max) //2
        if d[mid] < A[i]:
          min = mid+1
        else:
          max = mid-1
          save = mid
          
      d[save] = A[i]
  print(len(d)-1)
LIS()
