import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

child = [0]*(N+1) # 자식: 부모

adjs = {i:[] for i in range(1,N+1)}
for _ in range(N-1):
    temp = list(map(int, input().split()))
    adjs[temp[0]].append(temp[1])
    adjs[temp[1]].append(temp[0])

que = deque([1])
while que:
    
    node = que.popleft()    
    for neighbor in adjs[node]:
        if child[neighbor] == 0:
            child[neighbor] = node
            que.append(neighbor)


for i in range(2,N+1):
    print(child[i])