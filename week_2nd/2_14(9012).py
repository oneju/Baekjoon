# 괄호
# https://www.acmicpc.net/problem/9012
T = int(input())

for _ in range(T):
    vps = input()
    cnt = 0
    ans = 'YES'
    for i in vps:
        if i == "(":
            cnt+=1
        else:            
            if cnt ==0:
                ans = 'NO'
                break
            else:
                cnt-=1
        print(cnt)
    if cnt > 0 and ans == 'YES': ans = 'NO'
    print(ans)