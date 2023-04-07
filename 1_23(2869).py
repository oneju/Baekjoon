#달팽이는 올라가고 싶다
A,B,V = input().split(" ")
a = int(A)
b = int(B)
v = int(V)

stat = 0
day = (v-b)//(a-b)
if (v-b)%(a-b) != 0:
    day+=1

print(day)