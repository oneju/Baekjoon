# 원 영역
# https://www.acmicpc.net/problem/10000
import sys
input = sys.stdin.readline
N = int(input().strip())

arr = []
for _ in range(N):
    x,y = map(int, input().strip().split(" "))
    arr.append([x-y,'s'])
    arr.append([x+y,'e'])
# start 와 end 로 오른쪽, 왼쪽 구분

arr.sort()

stk = []
cnt = 1

for i in range(N*2):
    x, y = arr[i]
    
    if not stk:
        # 스택 비어있으면 추가
        stk.append({'x':x,'y':y,'stat':0})
        continue
    
    if y == 'e':
        # 원이 하나 끝나면 area 추가
        cnt+=1
        
        if stk[-1]['stat'] == 1:
            cnt+=1
        stk.pop()
        
        # 다음 점과 접점 여부 확인 (마지막 값이 아니면서, x 가 같지 않을때)
        if i != N*2-1 and arr[i+1][0] != x:
                stk[-1]['stat'] = 0
      
    else:
        # 스택의 마지막 좌표와 위치가 같을 때, 상태 1로 바꿈
        if stk[-1]['x'] == x:
            stk[-1]['stat'] = 1
        stk.append({'x':x,'y':y,'stat':0})
print(cnt)