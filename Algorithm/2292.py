import sys
input = sys.stdin.readline
n = int(input())
num = ans = 1
for i in range(n):
    num+=(6*i)
    if num >= n:
        print(i+1)
        break