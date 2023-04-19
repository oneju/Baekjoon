# 곱셈
# https://www.acmicpc.net/problem/1629
import sys
input = sys.stdin.readline
A, B, C = map(int, input().split())
'''
분할 A**(M+N) = A**M * A**N 지수 법칙
정복 (A*B)%C = (A%C)*(B%C) %C 나머지 분리 법칙
'''
cal = 0
def divide(a,b,c):
    global cal
    if b > 1:
        cal = divide(a,b//2,c) # 10 5 12
        if b % 2 == 1:
            return cal * cal * a % c 
        else:
            return cal * cal % c # 10 * 10 % 12 = 4
            
    elif b==1:
        return a%c # 10 % 12 = 10
    
print(divide(A,B,C)) # 5