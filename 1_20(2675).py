#문자열 반복
T = int(input())
for i in range(0,T):
    a,b = input().split(" ")
    R = int(a)
    S = str(b)
    P= ""
    for i in range(0,len(S)):
        P += S[i:i+1] * R
    print(P)