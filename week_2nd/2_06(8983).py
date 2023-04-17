# 사냥꾼
# https://www.acmicpc.net/problem/8983
import sys
input = sys.stdin.readline
M, N, L = map(int, input().strip().split(" "))
place = list(map(int,input().strip().split(" ")))
lst = []

for _ in range(N):
    lst.append(list(map(int,input().strip().split(" "))))
    
lst.sort()
place.sort()

cnt = 0
for anim in lst:
  e = M-1
  s = 0
  
  while s <= e:
    mid = (s+e) // 2
    h = abs(anim[0]-place[mid]) + anim[1]
  
    if h <= L:
        cnt += 1
        break
    elif place[mid] < anim[0]:
      s = mid +1
    else:
      e = mid-1
  
  
print(cnt)