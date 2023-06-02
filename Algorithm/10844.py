# 쉬운 계단 수
# https://www.acmicpc.net/problem/10844
n = int(input())
table = [[0]*10 for _ in range(n)]
for i in range(n):
    if i == 0:
        for idx in range(1,10):
            table[i][idx] = 1
        continue
    
    for j in range(0,10):
        if j==0:
            table[i][j] = table[i-1][1]
        elif j==9:
            table[i][j] = table[i-1][8]
        else:
            table[i][j] = table[i-1][j+1] + table[i-1][j-1]
print(sum(table[n-1])%1000000000)