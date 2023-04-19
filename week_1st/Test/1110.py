# 더하기 사이클 - 수학, 구현
import sys
N = int(sys.stdin.readline())
cnt = 0
new = N
while True:
    a = new // 10
    b = new % 10
    new = (b *10) + ((a+b)%10)
    
    cnt +=1
    if new == N:
        break
print(cnt)