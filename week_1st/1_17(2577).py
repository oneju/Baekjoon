#숫자의 개수
mul = 1
for i in range(0,3):
    num = int(input())
    mul *= num
mul = str(mul)
for i in range(0,10):
    cnt = mul.count(str(i))
    print(cnt)
