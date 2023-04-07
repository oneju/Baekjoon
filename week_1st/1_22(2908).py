#상수
a,b = input().split(" ")
num_1 = a[2]+a[1]+a[0]
num_2 = b[2]+b[1]+b[0]
sangsu = max(int(num_1),int(num_2))
print(sangsu)