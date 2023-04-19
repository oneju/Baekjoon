# 색종이 만들기
# https://www.acmicpc.net/problem/2630
import sys
input = sys.stdin.readline
N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split(" "))))

'''
종이를 1/4로 나눠서 탐색시작
만약 종이에 0,1이 존재하면 다시 1/4 분할 (recursion)
0만 존재하면 0 카운트 1
1만 존재하면 1 카운트 1
'''
zero_cnt = 0
one_cnt = 0

def papel(i,j,n):
    global zero_cnt, one_cnt
    x = []
    cur = paper[i][j]
    flag = 0
    for a in range(i,i+n):
        for b in range(j, j+n):
            if cur != paper[a][b]:
                flag = 1
                break
        if flag == 1:
            break
    if flag == 1:
        n //= 2
        papel(i,j,n)        # 1사분면
        papel(i,j+n,n)      # 2사분면
        papel(i+n,j,n)      # 3사분면
        papel(i+n,j+n,n)    # 4사분면
    
    elif cur == 0:
        zero_cnt += 1
        return
    else:
        one_cnt += 1
        return

papel(0,0,N)
print(zero_cnt)
print(one_cnt)