#하노이 탑
'''
1-1 2**1-1
2-3 2**2-1
3-7 2**3-1
4-15
5-31
'''
import sys

def Hanoi(no:int, a:int, b:int):
    if no > 1:
        Hanoi(no-1,a,6-a-b)
    
    print(f"{a} {b}")
    
    if no > 1:
        Hanoi(no-1,6-a-b,b)

N = int(sys.stdin.readline())

cnt = 2**N -1
print(cnt)

if N <=20:
    Hanoi(N,1,3)