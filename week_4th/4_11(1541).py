# 잃어버린 괄호
# https://www.acmicpc.net/problem/1541
string = input().split('-')
ans = 0
arr = []
for s in string:
    lst = s.split('+')
    pl = 0
    for i in lst:
        pl+=int(i)
    arr.append(pl)
ans = arr[0]
for a in arr[1:]:
    ans-=a
print(ans)
