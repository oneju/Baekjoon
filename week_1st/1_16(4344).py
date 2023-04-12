#평균은 넘겠지
C = int(input())
for i in range(0,C):
    case = input().split(" ")
    n = int(case[0])
    sum=0
    for j in range(0,n):
        sum+=int(case[j+1])
    avg = sum/int(n)
    cnt =0
    for score in case[1:n]:
        if score > avg:
            cnt+=1
    print("{:.3f}%".format(cnt/n * 100))
    
    