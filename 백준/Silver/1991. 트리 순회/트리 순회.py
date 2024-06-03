import sys
input = sys.stdin.readline

# recursion
N = int(input())

tree = {}

for _ in range(N):
    temp = input().split()
    tree[temp[0]] = temp[1:]

# preorder: 루트 -> 왼쪽 -> 오른쪽
def pre(node):
    global ans
    ans += node
    
    if tree[node][0] != '.':
        pre(tree[node][0])
    if tree[node][1] != '.':
        pre(tree[node][1])

# inorder: 왼쪽 -> 루트 -> 오른쪽
def inorder(node):
    global ans
    if tree[node][0] != '.':
        inorder(tree[node][0])
    
    ans += node
    
    if tree[node][1] != '.':
        inorder(tree[node][1])

# postorder: 왼쪽 -> 오른쪽 -> 루트
def post(node):
    global ans
    if tree[node][0] != '.':
        post(tree[node][0])
    if tree[node][1] != '.':
        post(tree[node][1])
    
    ans += node

ans = ''
pre('A')
print(ans)

ans = ''
inorder('A')
print(ans)

ans = ''
post('A')
print(ans)