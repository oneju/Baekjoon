# 인사성 밝은 곰곰이
# https://www.acmicpc.net/problem/25192
import sys
input = sys.stdin.readline
n = int(input())
gg = []
ans = 0
for _ in range(n):
    chat = input().strip()
    if chat == 'ENTER':
        gom = set(gg)
        ans += len(gom)
        gg = []
        continue
    gg.append(chat)
gom = set(gg)
ans+=len(gom)
print(ans)