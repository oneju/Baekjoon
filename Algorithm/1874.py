# 스택 수열
# https://www.acmicpc.net/problem/1874
import sys
input = sys.stdin.readline
n = int(input())
S = '+\n'
stack = [1]
check = 2
a = 0
for _ in range(n):
    num = int(input())
    while num >= check:
        stack.append(check)
        check+=1
        S+='+\n'
    if stack[-1]==num:
        p = stack.pop()
        S+='-\n'
    else:
        S = 'NO'
        break
print(S)