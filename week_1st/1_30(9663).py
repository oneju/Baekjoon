#N-Queen

import sys
input = sys.stdin.readline
N = int(input())

pos = [0] * N
flag_a = [False] * N         # 정복당한 row
flag_b = [False] * (2*N-1)   # 정복당한 대각선 b (대각선이 2*N-1개)
flag_c = [False] * (2*N-1)   # 정복당한 대각선 c

cnt = 0                      # 방법 개수 구하기

def set(i):
    global cnt
    
    for j in range(N):
        if(not flag_a[j] and
           not flag_b[i+j] and
           not flag_c[i-j+N-1]):
            pos[i] = j
            if i==N-1:
                cnt+=1
            else:
                flag_a[j] = flag_b[i+j] = flag_c[i-j+N-1] = True
                set(i+1)
                flag_a[j] = flag_b[i+j] = flag_c[i-j+N-1] = False
set(0)
print(cnt)