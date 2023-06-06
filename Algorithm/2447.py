# 별 찍기 - 10
# https://www.acmicpc.net/problem/2447
N = int(input())
check = [['*'] * N for _ in range(N)]
def star(n,x,y):
    if n == 3:
        check[x+1][y+1] = ' '
        return
    n//=3
    bin_x = x+n
    bin_y = y+n
    for i in range(n):
        for j in range(n):
            check[bin_x+i][bin_y+j] = ' '
    for i in range(3):
        for j in range(3):
            if i==1 and j==1:continue
            star(n,x+(n*i),y+(n*j))

star(N,0,0)

for i in range(N) :
    for j in range(N) :
        print(check[i][j], end="")
    print()