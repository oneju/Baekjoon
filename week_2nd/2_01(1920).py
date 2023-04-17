# 수 찾기
# https://www.acmicpc.net/problem/1920
import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().strip().split()))

A.sort()

M = int(sys.stdin.readline())
X = list(map(int,sys.stdin.readline().strip().split()))

for i in X:
  key = i
  pl = 0
  pr = len(A) -1
  while True:
    pc = (pl+pr)//2
    if A[pc] == key:    
      print(1) 
      break       
    elif A[pc]<key:     
      pl = pc+1
    else:
      pr = pc-1
    if pl>pr:
      print(0)
      break