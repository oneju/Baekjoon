# 단어 정렬
N = int(input())
lst = []

for i in range(N):
    string = input()
    if string not in lst:
        lst.append(string)

arr = sorted(lst, key=lambda x: (len(x), x))  # lambda x: 정렬 기준

for i in range(len(arr)):
    print(arr[i])
