#OX퀴즈
N = int(input())
for i in range(0,N):
    test_case = input()
    score=0
    cnt=0
    for i in range(0,len(test_case)):
        test = test_case[i:i+1]
        if test == "O":
            cnt+=1
        else:
            cnt=0
        score += cnt
    print(score)