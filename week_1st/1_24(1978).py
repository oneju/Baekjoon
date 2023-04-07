# 소수 찾기
N = int(input())
numlst = input().split(" ")
cnt = 0

for i in numlst:
    num = int(i)
    
    r = 0
    if num == 1:
        r=1
    else:
        for j in range(2,num):
            if num % j == 0:
                r+=1
                break;
    if r==0:
        cnt +=1

print(cnt)