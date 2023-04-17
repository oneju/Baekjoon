# 괄호의 값
# https://www.acmicpc.net/problem/2504
import sys
input = sys.stdin.readline

string = input().strip()
'''
() = 2
[] = 3
(x) = 2 * x
[x] = 3 * x
xy = x+y

(()[[]])([])
28

'''
stack = []
ret = 0
val = 1

for i in range(len(string)):
    # 여는 괄호일 경우
    if string[i] == '(': 
        val *= 2
        stack.append(string[i])
    elif string[i] == '[': 
        val *= 3
        stack.append(string[i])
        
    # 닫는 괄호일 경우    
    else:
        # 여는 괄호가 없다면 탈출
        if not stack:
            ret = 0
            break
        if string[i] == ')' and stack[-1] == '(':
            # 이전에 닫는 괄호가 있으면 더하기 생략 (중복으로 더해지는 것을 피해야하기 때문에..!)
            if string[i-1] not in [']',')']:
                ret += val
            val //= 2
            
        elif string[i] == ']' and stack[-1] == '[':
            if string[i-1] not in [']',')']:
                ret += val            
            val //= 3
        else:
            ret=0
            break
        stack.pop()                
if stack:
    ret = 0
print(ret)