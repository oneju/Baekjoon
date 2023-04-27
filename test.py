# 2152
import sys
input = sys.stdin.readline
n,m,s,t = map(int,input().split())
cities = [[] for _ in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    cities[a-1].append(b-1)

stack = []
visited = [0] * n
flag = 0
count = 0

def topolo():
    stack.append(s-1)
    visited[s-1] = 1
    global flag, count
    while stack:
        cur = stack.pop()
        if visited.count(1) == n:
            count = n
            flag = 1
            return
        
        for next in cities[cur]:
            visited[next] = 1
            stack.append(next)
            if next == (t-1):
                count = max(count, visited.count(1))
                flag = 1
    return

topolo()
if flag == 0:print(0)
else:print(count)