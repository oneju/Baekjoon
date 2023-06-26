# 팰린드롬 만들기
# https://www.acmicpc.net/problem/1213
import sys
input = sys.stdin.readline
Alph = list(input().strip())
length = len(Alph)
Name = ['']*length
A_dic = {}
for i in range(length):
    if Alph[i] in A_dic:
        A_dic[Alph[i]]+=1
    else:
        A_dic[Alph[i]] = 1
A_lst = sorted(A_dic.keys())
A_idx = N_idx = 0
while A_idx < len(A_lst):
    if A_dic[A_lst[A_idx]] >= 2:
        Name[N_idx] = Name[length - N_idx - 1] = A_lst[A_idx]
        A_dic[A_lst[A_idx]] -= 2
        N_idx += 1
    else:
        A_idx += 1
# value = 1인 애들만 남은 상태 -> 이게 둘 이상이면 실패
A = 0
for i in range(len(A_lst)):
    if A_dic[A_lst[i]] == 1:
        if A == 0:
            Name[N_idx] = A_lst[i]
            A = 1
        else:
            A = 2
            break

if A == 2:
    print("I'm Sorry Hansoo")
else:
    print(''.join(Name))