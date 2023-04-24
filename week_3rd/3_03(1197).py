# 최소 스패닝 트리
# https://www.acmicpc.net/problem/1197
import sys
input = sys.stdin.readline
V,E = map(int,input().split())
e_lst = [list(map(int,input().split()))for _ in range(E)]
e_lst.sort(key = lambda x:x[2])

parent = [i for i in range(V+1)] # 집합 부모 확인

def find_parent(x):
    # 만약 visited[x] 값이 자신이 아니라면 부모 를 찾아가겠다
    if parent[x]==x:
        return x
    else:
        return find_parent(parent[x]) 

def MST(x,y):
    # 집합의 부모가 다를 때 실행
    # 부모가 더 작은 걸로 변환
    a = find_parent(x)
    b = find_parent(y)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

sum = 0
for x,y,w in e_lst:
    # edge 에서 x, y, w 를 가져와서 비교, 계산
    if find_parent(x) != find_parent(y):
        MST(x,y)
        sum+=w
        
print(sum)
# 프림 MST 알고리즘 (min_heap)
'''
import sys
import heapq
import collections

V, E = map(int, sys.stdin.readline().split())
matrix = collections.defaultdict(list) # 빈 리스트 생성
for _ in range(E) :
    x, y, weight = map(int, sys.stdin.readline().split())
    # 무방향 그래프 표현
    # 0번 부터 V-1번까지 노드라고 생각한다.(문제상에는 1 ~ V 까지)
    matrix[x-1].append([weight, x-1, y-1])
    matrix[y-1].append([weight, y-1, x-1])

def primMST(v) :
    node = [0] * V # 방문 여부를 저장할 배열
    # 시작 정점 방문
    node[v] = 1
    # 시작노드에서 갈 수 있는 모든 간선 리스트
    candidate = matrix[v] 
    heapq.heapify(candidate) # 우선순위 큐로 변환
    sum = 0
    while candidate :
        weight, x, y = heapq.heappop(candidate)
        # 정점 y를 방문한 적이 없다면
        if node[y] == 0 :
            node[y] = 1
            sum += weight
            
            # y에서 갈 수 있는 모든 간선에 대한 정보 중에서
            # 방문한 적이 없는 노드들만 candidate에 저장
            for edge in matrix[y] :
                if node[edge[2]] == 0 :
                    heapq.heappush(candidate, edge)
    print(sum)

primMST(0)
'''