# LCS
# https://www.acmicpc.net/problem/9251
import sys
input = sys.stdin.readline
s1 = input().strip()
s2 = input().strip()

arr = [[['',0] for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]

for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1] == s2[j-1]:
            arr[j][i][0] = ''.join([arr[j-1][i-1][0], s1[i-1]])
            arr[j][i][1] = arr[j-1][i-1][1] + 1
        else:
            if arr[j-1][i][1] > arr[j][i-1][1]:arr[j][i] = arr[j-1][i]
            else:arr[j][i] = arr[j][i-1]
'''
ACAYKP
CAPCAK

ACAK 4
'''
print(*arr[-1][-1])