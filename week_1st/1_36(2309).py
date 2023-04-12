#일곱 난쟁이
'''
9개의 숫자 데이터를 받아서 -> 7개의 숫자 배열로 출력
조건 : 7 개의 숫자의 합 = 100, 오름차순 정렬
'''
#num_lst = [20,7,23,19,10,15,25,8,13]
import sys
num_lst =  [int(sys.stdin.readline()) for _ in range(9)]
num_lst.sort()

lst_sum = sum(num_lst)

for i in range(8):
    for j in range(i+1,9):
        if lst_sum -(num_lst[i] + num_lst[j]) == 100:
            num_lst[i] = num_lst[j] = 0
            num_lst.sort()
            [print(num_lst[k]) for k in range(2,9)] 
            exit()