import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
temp = [0]

for i in range(1, n + 1):
    temp.append(arr[i - 1] + temp[i - 1])

for i in range(m):
    a, b = map(int, input().split())
    print(temp[b] - temp[a - 1])