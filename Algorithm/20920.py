# 영단어 암기는 괴로워
# https://www.acmicpc.net/problem/20920
import sys
input = sys.stdin.readline
n,m = map(int,input().split())
mem = {}
for _ in range(n):
    word = input().strip()
    if len(word) >= m:
        if word in mem:mem[word]+=1
        else:mem[word] = 1
mem = sorted(mem.items(), key=lambda x:(-x[1],-len(x[0]),x[0]))
[print(word[0])for word in mem]