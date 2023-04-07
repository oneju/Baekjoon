#단어의 개수
lst = input().split(" ")
cnt = len(lst)
if lst.count('')>=1:
    cnt -= lst.count('')
print(cnt)