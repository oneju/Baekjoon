# 색종이
# https://www.acmicpc.net/problem/2563
'''
검은색 영역 = 색종이 넓이 - 겹치는 부분 넓이
겹치는 부분이 없다면 색종이 넓이 : 100 이 추가 
겹치는 부분이 있다면 겹치는 부분 넓이 : 10-xx-x * 10-yy-y 를 빼준다
겹치는 부분 : 
'''
import sys
input = sys.stdin.readline
n = int(input())
paper = [[0]*100 for _ in range(100)]
width = 0
for _ in range(n):
    x,y = map(int,input().split())
    for i in range(10):
        for j in range(10):
            if paper[x+i][y+j]==0:
                paper[x+i][y+j]=1
                width +=1
# arr = [list(map(int,input().split()))for _ in range(n)]
# arr.sort()
# width = 100
# for i in range(1,n):
    
#     if (arr[i][0] - arr[i-1][0]) < 10 and (arr[i][1] - arr[i-1][1]) < 10:
#         width -= ((10 - abs(arr[i][0] - arr[i-1][0])) * (10 - abs(arr[i][1] - arr[i-1][1])))
#     width+=100
print(width)