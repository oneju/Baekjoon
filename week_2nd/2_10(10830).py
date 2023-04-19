# 행렬 제곱
# https://www.acmicpc.net/problem/10830
import sys
input = sys.stdin.readline
N,B = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))
    
def mul(lst_1,lst_2):
    # [[0]*N]*N 이런식으로 하면 고정 주소때문에 값에 오류가 생긴다
    n_lst = [[0] * N for _ in range(N)]
    
    for i in range(N): # 0
        for j in range(N): # 0,1
            for k in range(N): # 0,1,0
                # 행렬 곱셈 계산하는 식
                n_lst[i][j] += lst_1[i][k] * lst_2[k][j] # [0][0] = [0,0]*[0,0]+[0,1]*[1,0]
                
            n_lst[i][j]%=1000
    return n_lst

def divide(lst, b):
    if b==1:
        # tmp에 저장하는 값
        for i in range(N) :
            for j in range(N) :
                lst[i][j] %= 1000
        return lst
    else:
        tmp = divide(lst, b//2)
        if b%2 == 0:
            return mul(tmp, tmp)
        else: # 제곱의 크기가 홀수일 경우에 남은 한 배열도 계산을 해준다
            return mul(mul(tmp,tmp),lst)
ans = divide(lst, B)

for a in ans:
    print(*a)