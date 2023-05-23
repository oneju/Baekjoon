# 통계학
# https://www.acmicpc.net/problem/2108
import sys
input = sys.stdin.readline
n = int(input())
dic = {}
lst = []
for _ in range(n):
    num = int(input())
    lst.append(num)
    if num in dic: dic[num]+=1
    else: dic[num] = 1
dic_key = sorted(lst)
print(round(sum(dic_key)/n)) # 산술평균
print(dic_key[(n//2)]) # 중앙값
# 최빈값
dic = sorted(dic.items(),key = lambda x:(-x[1],x[0]))
if n>1 and dic[0][1] == dic[1][1]:print(dic[1][0])
else:print(dic[0][0])
print(dic_key[-1]-dic_key[0]) # 범위
