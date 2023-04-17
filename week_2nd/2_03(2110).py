# 공유기 설치
# https://www.acmicpc.net/problem/2110
import sys
input = sys.stdin.readline
N, C = map(int, input().strip().split(" "))
pos = [int(input().strip()) for _ in range(N)]

pos.sort()

min = 1
max = pos[N-1] - pos[0]  # 최대 차이
ans = 0

# recursion error

'''
def search(cnt, idx, mid):
  for i in range(idx+1,N):
    if (pos[i]- pos[idx]) >= mid:
      return search(cnt+1,i, mid)
  return cnt
'''

while min <= max:
    mid = (min + max) // 2
    cnt = 1
    idx = 0
    
    for i in range(1,N):
        if (pos[i] - pos[idx]) >= mid :
            cnt += 1
            idx = i
                    
    if cnt >= C:
        min = mid+1
        
    else:
        max = mid-1
        
print(mid)