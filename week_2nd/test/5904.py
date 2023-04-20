# Moo 게임
import sys
input = sys.stdin.readline
N = int(input())
# N번째 위치에 있는 문자

S = 3
k = 0

def divide (S, mid, n):
    left = (S-mid)//2
    
    if n in range(left+1, left+mid+1):
        # 가운데
        if n-left == 1: return 'm'
        else: return 'o'
        
    if n > left+mid:
        # 오른쪽
        n -= (left+mid)
        
    return divide(left, mid-1, n)

while S < N:
    k+=1
    S = 2 * S + k + 3
    
print(divide(S, k+3, N))