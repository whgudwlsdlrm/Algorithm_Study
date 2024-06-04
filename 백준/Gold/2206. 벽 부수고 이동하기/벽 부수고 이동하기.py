import sys
from collections import deque
# input = sys.stdin.readline

N,M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(input().rstrip())

# BFS deque([(거리, 좌표, 벽 안뚫 여부)])
que = deque([(1,(0,0),1)])
visited = [[False]*M for _ in range(N)]

ans = []
while que:
    dist, (y,x), hist = que.popleft()
    
    if (y,x) == (N-1,M-1):
        ans.append(dist)
        if hist:
            break

    if visited[y][x] == hist:
        continue
    if visited[y][x] and hist==2:
        continue
        
    # 안쓰고 통과 -> True / 쓰고 통과 -> 여전히 False    
    visited[y][x] = hist
    
    for coord in ((y,x-1), (y,x+1), (y-1,x), (y+1,x)):
    
        if 0<=coord[0]<N and 0<=coord[1]<M: #y,x
            if graph[coord[0]][coord[1]] == '0':
                que.append((dist+1, (coord[0], coord[1]), hist))
            elif hist == 1:
                que.append((dist+1, (coord[0], coord[1]), 2))

if ans:
    print(min(ans))
else:
    print(-1)