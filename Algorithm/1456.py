# 거의 소수
# https://www.acmicpc.net/problem/1456
import sys
input = sys.stdin.readline
A,B = map(int,input().split())
def eratos(N):
    lst = [True for _ in range(N+1)]
    lst[0] = lst[1] = False
    for i in range(2,(len(lst)//2)+1):
        if lst[i]:
            a = 2
            while i*a < len(lst):
                if lst[i*a]:
                    lst[i*a] = False
                a+=1
    return lst
cnt = 0
prime_lst = eratos(int(B**0.5))
# 못풀음
# 소수들을 돌면서 값을 계산해서 카운팅하는 방식으로 가야함
# 아니면 좀 막막해
for num in range(2,len(prime_lst)):
    if prime_lst[num]:
        S = 2
        while num ** S <= B:
            if num ** S >= A:
                cnt+=1
            S+=1
print(cnt)