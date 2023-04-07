#한수
'''
N 을 받아서 
1부터 N까지의 자연 수 중에서 
한수 : 각 자릿수 간에 등차수열을 이루는 수
의 개수를 구하려면

100 이상의 수 중에서 
111
123
135
147
'''

N = int(input())
if N < 100:
    print(N)
else :
    
    count =99
    for num in range(100,N+1): # 120
        digit = 10
        lst = []
        cnt = 0
        while num // 10 > 0: #120, digit10  num = 12 num = 1  
            lst.append(num%digit) #120%10 = 0 12%10 = 2
            num//=digit #lst=[0], num = 12 lst=[0,2] num = 1
        lst.append(num)
        
        for i in range(1,len(lst)-1):
            
            if (lst[i+1]-lst[i]) == (lst[1]-lst[0]):
                
                cnt+=1
            else:
                break
            
        if cnt == (len(lst)-2):
            
            count+=1
    print(count)