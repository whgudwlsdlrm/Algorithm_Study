import sys
from collections import deque

input = sys.stdin.readline

# 노드 지우기: 해당 노드 ~ 리프노드
# N: 50이하의 자연수 / 노드번호: 0~N-1번
# 리프노드의 개수


N = int(input())
parents = list(map(int, input().split()))
delete = int(input())

tree = [ [] for _ in range(N) ]
for child,parent in enumerate(parents):
    if parent == -1:
        start = child
    elif child == delete:
        continue
    else:
        tree[parent].append(child)

# 원래 자식노드가 1개 있었는데 -> 그게 없어지면 부모노드는 리프노드가 되겠네요

que = deque([start])
leaf = 0
while que:
    
    node = que.popleft()
    if node == delete:
        continue
    
    if len(tree[node]) == 0:
        leaf += 1
    else:
        
        for child in tree[node]:
            que.append(child)

print(leaf)