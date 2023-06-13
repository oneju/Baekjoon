# 신기한 소수
# https://www.acmicpc.net/problem/2023
import sys
N = int(sys.stdin.readline())
def isprime(num):
    for i in range(2,int(num**(1/2))+1):
        if num%i == 0:
            return 1
    return 0

def special(num, cnt):
    if cnt == N:
        print(num)
        return 
    for i in range(10):
        new = num*10 + i
        if isprime(new) == 1:
            continue
        special(new,cnt+1)

for i in [2,3,5,7]:
    special(i, 1)