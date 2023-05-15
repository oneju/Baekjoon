# 인사성 밝은 곰곰이
# https://www.acmicpc.net/problem/25192
import sys
input = sys.stdin.readline
n = int(input())
gg = set()
ans = 0
for _ in range(n):
    chat = input().strip()
    if chat == 'ENTER':
        ans += len(gg)
        gg = set()
        continue
    gg.add(chat)
gom = set(gg)
ans+=len(gom)
print(ans)