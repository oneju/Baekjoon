# 스카이라인
N = int(input())
buildings = [list(map(int, input().split())) for _ in range(N)]

buildings.sort(key = lambda x:x[2])
print(buildings)

stack = []
end = 0

for building in buildings:
    print(stack)
    # heap 비어있으면 추가
    if not stack:
        stack.append(building[:2])
        end = building[2]
        
    # end 가 building 의 끝 보다 짧으면서, 높이가 낮다면, pop
    # [[1, 11], [3, 13], [9, 0], [16, 0], [19, 18], [23, 13], [29, 0]]
    
    if stack and (building[1] > stack[-1][1] ):
        stack.pop()
    if building[0] > end:
        stack.append([end, 0])
    if building[0] < end and building[1] < stack[-1][1]:
        stack.append([end,building[1]])
    if building[2] > end:
        stack.append(building[:2])
        end = building[2]
stack.append([end,0])
print(stack)
# [print(stack[i][0], stack[i][1], end=" ") for i in range(len(stack))]