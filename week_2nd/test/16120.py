# PPAP
# https://www.acmicpc.net/problem/16120
import sys
input = sys.stdin.readline
S = input().strip()
'''
review
1.	ppap는 입력받은 값을 stack에 하나 씩 append 할 때 마다,
2.	스택의 [-4:] 를 ppap인지 확인하여 ppap를 pop해서 지워준 후,
3.	p를 추가하면 됩니다.
4.	그리고 스택이 p이면 ppap를 출력하고 아닐경우 np를 출력합니다.
'''
stack = []
ppap = ['P','P','A','P']
for a in S:
    stack.append(a)
    if stack[-4:] == ppap:
        for _ in range(3):stack.pop()
        
if stack == ['P']:
    print("PPAP")
else:
    print("NP")