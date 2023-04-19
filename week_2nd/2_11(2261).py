# 가장 가까운 두 점
# https://www.acmicpc.net/problem/2261
import sys
input = sys.stdin.readline
n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]
lst.sort()

'''
가장 가까운 두 점 사이의 거리 ** 2
분할 : 최소범위, 점 두개가 남으면
정복 : (a1-a2) ** 2 + (b1-b2) ** 2 의 최소값
결합 : 합치면서, 전체 최소값 도출
'''
min_length = sys.maxsize
def divide(s,e):
    global min_length
    if e == s: return sys.maxsize
    elif e-s == 1:
        a = (lst[e][0] - lst[s][0]) ** 2
        b = (lst[e][1] - lst[s][1]) ** 2
        return a+b
    else:
        mid = (s+e)//2
        
        left = divide(s, mid)
        right = divide(mid,e)
        
        min_length = min(left, right)
        
        # 왼쪽, 오른쪽 탐색 후, 결합하며 탐색
        check_point = []
        divide_x = lst[mid][0]
        
        for i in range(s, e+1):
            if (lst[i][0] - divide_x)**2 <= min_length:
                check_point.append(lst[i])
        check_point.sort(key=lambda x:x[1])
        
        for i in range(len(check_point)):
            now = check_point[i]
            for j in range(i+1, len(check_point)):
                compare = check_point[j]
                if (compare[1] - now[1])**2 >= min_length:
                    break
                dist = (now[0] - compare[0])**2 + (now[1] - compare[1])**2
                min_length = min(min_length, dist)
        
        
        return min_length

print(divide(0,n-1))