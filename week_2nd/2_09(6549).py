# 히스토그램에서 가장 큰 직사각형
# https://www.acmicpc.net/problem/6549
import sys
input = sys.stdin.readline

'''
분할 : 크기가 1이 될 때 까지 분할
정복 : 너비를 구한다면
결합 : 한 단계씩 비교해가며 최대값을 구한다

https://st-lab.tistory.com/255
'''
def cal_area(l,r,mid,lst):
    left = mid
    right = mid
    height = lst[mid]
    area = height
    # left, right 값이 범위 내에 존재하다면,
    while left > l and right < r:
        if lst[left-1] > lst[right+1]:
            left-=1
            # 가장 작은 값 높이에 저장
            height = min(height,lst[left])
        else:
            right+=1
            height = min(height,lst[right])
        # wide = height * width 의 최대값
        area = max(area, height * (right - left + 1))
    # right 값이 아직 존재하다면, 
    while right < r:
        right +=1
        height = min(height,lst[right])
        area = max(area, height * (right - left + 1))
    # left 값이 아직 존재하다면, 
    while left > l:
        left-=1
        height = min(height,lst[left])
        area = max(area, height * (right - left + 1))
    return area

def divide(l, r, lst):
    if l == r:
        # 너비가 1이면 넓이는 높이
        return lst[l]
    
    mid = (l+r)//2
    # 가운데를 기준으로 왼쪽 오른쪽으로 공간을 나눠서
    l_area = divide(l, mid, lst)
    r_area = divide(mid+1, r, lst)
    # 그중 넓이가 더 넓은 부분 저장
    val = max(l_area, r_area)
    # 합쳐지는 부분의 넓이 구하기
    val = max(val, cal_area(l,r,mid,lst))
    return val



while True:
    a = input().split()
    if a[0] == '0':
        break
    in_std = list(map(int, a))
    n = in_std[0]
    lst = in_std[1:1+n]
    print(divide(0, n-1, lst))
    