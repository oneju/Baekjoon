# 그룹 단어 체커
# https://www.acmicpc.net/problem/1316
import sys
input = sys.stdin.readline
N = int(input())
'''
그룹단어 : 단어에 존재하는 모든 문자에 대해서, 각 문자가 연속해서 나타나는 경우
ccazzzzbb -> 그룹단어
aabbbccb -> 그룹단어 아님
'''
cnt = 0
for _ in range(N):
    S = input()
    a = 0
    arr = []
    for i in range(len(S)):
        if S[i:i+1] == S[i-1:i]:continue
        if S[i:i+1] not in arr:
            arr.append(S[i:i+1])
        else:
            a = 1
            break
    if a==0:cnt+=1
print(cnt)