#골드바흐의 추측
def isPrime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

N = int(input())
for i in range(N):
    n = int(input())
    for a in range(n//2,1,-1):
        b = n-a
        if (isPrime(a)==True)and(isPrime(b)==True):
            print(f"{a} {b}")
            break
