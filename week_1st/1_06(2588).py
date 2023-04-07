#곱셈
a = int(input())
str_b = input()

for i in range(3,0,-1):
    m = a*int(str_b[i-1:i])
    print(m)
print(a*int(str_b))    
