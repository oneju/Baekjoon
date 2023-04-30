# 잃어버린 괄호
# https://www.acmicpc.net/problem/1541
string = input().split('-')
ans = 0
arr = []
for s in string:
    pl = sum(list(map(int,s.split('+'))))
    arr.append(pl)
ans = arr[0]
for a in arr[1:]:
    ans-=a
print(ans)
