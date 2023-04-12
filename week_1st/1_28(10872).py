#팩토리얼
import sys
N = int(sys.stdin.readline())

def fact(n):
    if n>0:
        return n * fact(n-1)
    else:
        return 1

print(fact(N))

'''
factorial = 1
for i in range(1,N+1):
    factorial *= i
print(factorial)'''