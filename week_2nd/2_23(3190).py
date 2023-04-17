# 뱀
# https://www.acmicpc.net/problem/3190
import sys
from collections import deque
input = sys.stdin.readline
N = int(input().strip())
K = int(input().strip())

apple = [[0 for j in range(N+1)] for i in range(N+1)]
for _ in range(K):
    num = input().split(" ")
    apple[int(num[0])][int(num[1])]=1

L = int(input().strip())
dir = []
for _ in range(L):
    a,b = input().strip().split(" ")
    dir.append([int(a),b])

x = [0,1,0,-1] # 아래, 왼쪽, 위, 오른쪽
y = [1,0,-1,0]

time = 0
length = deque([(1,1)])
x_i = 1
y_i = 1
idx = 0
i = 0

while True:
    y_i += y[idx]
    x_i += x[idx]

    if y_i in range(1,N+1) and x_i in range(1,N+1) and (x_i,y_i) not in length:

        time+=1
        
        if length and apple[x_i][y_i]==0:
            length.popleft()
            
        else:
            apple[x_i][y_i]=0
        
        length.append((x_i,y_i))
            
        if i < L and time == dir[i][0]:
            if dir[i][1] == "D":
                idx=(idx+1)%4
            else:
                idx=(idx-1)%4
            i+=1
    else:
        break    
print(time+1)