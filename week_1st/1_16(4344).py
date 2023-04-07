#평균은 넘겠지
C = int(input())
for i in range(0,C):
    case = input().split(" ")
    n = int(case[0])
    sum=0
    score_lst = []
    for j in range(0,n):
        score_lst.append(int(case[j+1]))
        sum+=score_lst[j]
    avg = sum/int(n)
    cnt =0
    for score in score_lst:
        if score > avg:
            cnt+=1
    per = cnt/n * 100
    print("{:.3f}%".format(per))
    
    