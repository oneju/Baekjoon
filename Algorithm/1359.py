# 복권
# https://www.acmicpc.net/problem/1359
import sys
input = sys.stdin.readline
n,m,k = map(int,input().split())
'''
ans += mCk * (n-m)C(m-k) / nCm
'''
ans = 0
def Comb(num1,num2):
    num = 1
    for i in range(num1,num2,-1):
        num *= i
    return num
while m>=k:
    if n-m < m-k:
        k+=1
        continue
    ans += (Comb(m,k)*Comb(n-m,m-k))/Comb(n,m)
    k+=1
print(ans)