#최댓값
lst = []
for i in range(0,9):
    num = int(input())
    lst.append(num)
m = max(lst)
print(m)
print(lst.index(m)+1)