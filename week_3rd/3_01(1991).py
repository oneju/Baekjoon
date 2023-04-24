# 트리 순회
# https://www.acmicpc.net/problem/1991
import sys
input = sys.stdin.readline
class Node:
    def __init__(self, data):
        self.root = data
        self.left = None
        self.right = None

N = int(input())
N_list = [Node(chr(i+65)) for i in range(N)]

for i in range(N):
    arr = list(input().split())
    N_list[ord(arr[0])-65].left = N_list[ord(arr[1])-65] if arr[1] != '.' else None
    N_list[ord(arr[0])-65].right = N_list[ord(arr[2])-65] if arr[2] != '.' else None

pre_string = ''
def preorder(n):
    global pre_string
    
    pre_string += n.root
    # 왼쪽노드가 있으면 재귀
    if n.left != None: preorder(n.left)
    # 오른쪽노드가 있으면 재귀
    if n.right != None: preorder(n.right)
    # 자식이 없으면 return
    return

in_string = ''
def inorder(n):
    global in_string
    # 자식노드가 없다면 return
    if n.left == None and n.right == None:
        in_string+=n.root
        return
    # 왼노드가 있다면 재귀
    if n.left != None:inorder(n.left)
    # 나
    in_string += n.root
    # 오른노드가 있다면 재귀
    if n.right != None:inorder(n.right)
    
post_string = ''
def postorder(n):
    global post_string
    # 자식노드가 없다면 return
    if n.left == None and n.right == None:
        post_string+=n.root
        return
    # 왼노드가 있다면 재귀
    if n.left != None:postorder(n.left)
    # 오른노드가 있다면 재귀
    if n.right != None:postorder(n.right)
    # 없다면 나
    post_string += n.root
preorder(N_list[0])
inorder(N_list[0])
postorder(N_list[0])
print(f"{pre_string}\n{in_string}\n{post_string}")