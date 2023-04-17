# 크게 만들기
# https://www.acmicpc.net/problem/2812
import sys
input = sys.stdin.readline
N, K = map(int, input().strip().split(" "))
num = input().strip()

'''
1231234
3234
'''
stack = []
m = N-K

for i in range(N):
    # 스택에 값이 있으면서, 뺄 값이 남아있고, 스택 마지막값보다 크면 pop()
    while stack and K > 0 and num[i] > stack[-1]:
        stack.pop()
        K -= 1
    stack.append(num[i])
    
# 빼야할 값들이 다 빠지지 않을 수도 있으니, 고정 자릿수까지만 출력
print("".join(stack[:m]))