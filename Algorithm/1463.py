# 1로 만들기
# https://www.acmicpc.net/problem/1463
import sys
input = sys.stdin.readline
n = int(input())
mem = [sys.maxsize] * (n+1)
mem[1] = 1
'''
숫자를 1부터 올려가면서 확인한다
만약 숫자 계산했을때 계산한 인덱스에 값이 있다면 +1 해서 저장한다
'''
for i in range(2,n+1):
    mem[i] = mem[i-1]+1
    if i%6==0:
        mem[i] = min(mem[i//2]+1,mem[i//3]+1)
    else:
        if i%3==0:
            mem[i] = min(mem[i],mem[i//3]+1)
        if i%2==0:
            mem[i] = min(mem[i],mem[i//2]+1)
print(mem[n]-1)