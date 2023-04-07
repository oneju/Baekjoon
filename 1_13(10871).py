#X보다 작은 수
nx = input().split(" ")
N = int(nx[0])
X = int(nx[1])
A = input().split(" ")
for i in A:
	if int(i) < X:
		print(i , end=" ")