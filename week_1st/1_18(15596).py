#정수 N개의 합
#정수 리스트 a
#a의 길이 n
#a에 포함되어있는 정수의 합 return
def solve(a):
    n = len(a)
    sum=0
    for num in a:
        sum += num
    return sum