import sys
N,S = map(int, sys.stdin.readline().split(" "))
nums = list(map(int,sys.stdin.readline().split()))

arr = [] # 새로운 배열을 받을 변수
cnt = 0

def comb(start):
  global cnt
  # 만약 배열 길이가 0보다 크면서 조합 합계가 s 와 같으면 cnt 올리고 탈출
  if len(arr) > 0 and sum(arr) == S:
    cnt+=1
    # return 을 추가하면 함수가 끝나서 시작이 올라간 상태로 함수가 다시 시작돼
  
  # 배열에 첫 값 넣고
  for j in range(start,N):
    arr.append(nums[j])
    comb(j+1)
    arr.pop()

comb(0)
print(cnt)