n,m = map(int,input().split())
num_lst = [list(map(int,input().split())) for _ in range(n)]
sum_lst = [[0]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        sum_lst[i][j] = sum_lst[i-1][j] + sum_lst[i][j-1] + num_lst[i-1][j-1] - sum_lst[i-1][j-1]
        
for _ in range(m):
    x_1,y_1,x_2,y_2 = map(int,input().split())
    sum = sum_lst[x_2][y_2] - sum_lst[x_1-1][y_2] - sum_lst[x_2][y_1-1] + sum_lst[x_1-1][y_1-1]
    print(sum)