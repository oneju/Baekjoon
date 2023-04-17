# 스택
# https://www.acmicpc.net/problem/10828
import sys
input = sys.stdin.readline
N = int(input().strip()) # .strip() 으로 '\n' 없애기

arr = []
for i in range(N):
    lst = input().strip().split(' ')
    com = lst[0]
    
    if com == 'push':
        arr.append(lst[1])
    elif com == 'pop':
        if arr: print(arr.pop())
        else: print(-1)
    elif com == 'size':
        print(len(arr))
    elif com == 'top':
        if arr: print(arr[len(arr)-1])
        else: print(-1)
    elif com == 'empty':
        if arr: print(0)
        else: print(1)