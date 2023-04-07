#종이자르기
'''
w, h, n 입력받아서 (1:w) (1:h) 넓이의 종이를
n 번 자른다
0 *를 입력받을 경우 : 가로 *
1 *를 입력받을 경우 : 세로 *
잘려진 종이들 중 가장 넓은 종이의 넓이는?
'''
w,h = input().split(" ")
n = int(input())
w_lst =[0,int(w)]
h_lst =[0,int(h)]

for i in range(n):
    a,b = input().split(" ")
    if a=="1":
        w_lst.append(int(b))
    else:
        h_lst.append(int(b))

w_lst.sort()
h_lst.sort()
w_max =0
h_max= 0
for i in range(len(w_lst)-1):
    W = w_lst[i+1]-w_lst[i]
    w_max = max(w_max, W)
for i in  range(len(h_lst)-1):
    H = h_lst[i+1]-h_lst[i]
    h_max = max(h_max,H)
   
answer = w_max*h_max
print(answer)