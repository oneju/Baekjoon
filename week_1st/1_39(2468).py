# 안전 영역
'''

안전 영역 : 물에 잠기는 지역을 제외한 연속된 지역들
bfs

'''
import sys
# from collections import deque
N = int(sys.stdin.readline())
lst = [list(map(int, sys.stdin.readline().split(" "))) for _ in range(N)]


x = [-1, 1, 0, 0]    # 좌표별 상하좌우 확인 리스트 생성
y = [0, 0, -1, 1]

# 0,0 부터 시작해서 탐색 시작

max_cnt = 0

# 안전 영역 찾기 시~작
for rainfall in range(max(map(max, lst))):
    cnt=0
    visited = [[False]*N for _ in range(N)]  # 방문 확인 배열
    
    for i in range(N):
        for j in range(N):
            if lst[i][j] > rainfall and visited[i][j] == False:  # 해당 좌표를 방문한 적 없고, rainfall 보다 크다면
                queue = []                                       # queue를 만들어서 
                queue.append([i,j])                              # 현 좌표 넣고
                visited[i][j] = True                             # 방문 흔적 남기기
                    
                while queue:                                     # queue 에 값이 있는 동안에 반복
                    a,b = queue.pop(0)                           # 좌표빼내기
                    # 상하좌우 탐색 시작
                    for k in range(4):                           # 들어간 순서대로 빼내야하기 때문에 pop(0) : popleft()와 같은 역할
                        x_index = a+x[k]
                        y_index = b+y[k]
                        
                        if x_index > -1 and x_index < N and y_index > -1 and y_index < N:
                            if lst[x_index][y_index] > rainfall and visited[x_index][y_index] == False:
                                visited[x_index][y_index] = True
                                queue.append([x_index,y_index])
                
                cnt+=1           # queue가 비면, 영역 하나 count
    
    max_cnt = max(cnt,max_cnt)
print(max_cnt)