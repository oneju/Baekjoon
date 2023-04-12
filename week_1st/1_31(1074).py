#Z
'''
N을 받아서 
배열의 크기가 2**N * 2**N
if N>1 : 
4등분 2**N-1 * 2**N-1 크기로
'''
import sys
input = sys.stdin.readline
N,r,c = map(int, input().split())

def Z(n,r,c):
    if n==0:
        return 0
    else:
        return 2 * (r%2) + (c%2) + 4 * Z(n-1,r//2,c//2)
    #3,5,2  
    # 1 + 2 + 1 = (2*0+1) + (2*1+0) + (2*0+1) = 25
    #(2*1+1) + 4*(2*1+1) = 3*4+3 = 15

print(Z(N,r,c))