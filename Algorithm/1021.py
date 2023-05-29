# 회전하는 큐
# https://www.acmicpc.net/problem/1021
'''
[1,2,3,4,5,6,7,8,9,10]
1[2,3,4,5,6,7,8,9,10,1] -> 2 [3,4,5,6,7,8,9,10,1]
2[1,3,4,5,6,7,8,9,10]
3[10,1,3,4,5,6,7,8,9]
4[9,10,1,3,4,5,6,7,8] -> 9 [10,1,3,4,5,6,7,8]
5[1,3,4,5,6,7,8,10]
6[3,4,5,6,7,8,10,1]
7[4,5,6,7,8,10,1,3]
8[5,6,7,8,10,1,3,4] -> 5 
'''
import sys
from collections import deque
input = sys.stdin.readline
n,m = map(int,input().split())
queue = deque(i for i in range(1,n+1))
find = list(map(int,input().split()))
cnt = 0
for num in find:
    idx = queue.index(num)
    if idx == 0:
        queue.popleft()
    else:
        if idx > len(queue)//2:
            while queue[0]!=num:
                for i in range(len(queue)-1,0,-1):
                    temp = queue[i]
                    queue[i] = queue[i-1]
                    queue[i-1] = temp
                cnt+=1
        else:
            while queue[0]!=num:
                for i in range(1,len(queue)):
                    temp = queue[i]
                    queue[i] = queue[i-1]
                    queue[i-1] = temp
                cnt+=1
        queue.popleft()
print(cnt)
