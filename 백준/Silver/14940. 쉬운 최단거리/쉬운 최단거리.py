import sys
from collections import deque

input = sys.stdin.readline

N,M = map(int, input().split())
graph = []
for i in range(N):
    temp = list(map(int, input().split()))
    if 2 in temp:
        start_x, start_y = temp.index(2),i
    graph.append(temp)
    
visited = [[0]*M for _ in range(N)]

que = deque([(0,start_y,start_x)])
while que:
    distance,y,x = que.popleft()
    
    if visited[y][x] > 0:
        continue
    
    visited[y][x] = distance

    if x > 0:
        if graph[y][x-1] == 1:
            que.append((distance+1, y, x-1))
    if x < M-1:
        if graph[y][x+1] == 1:
            que.append((distance+1, y, x+1))
    if y > 0:
        if graph[y-1][x] == 1:
            que.append((distance+1, y-1, x))
    if y < N-1:
        if graph[y+1][x] == 1:
            que.append((distance+1, y+1, x))


for y in range(N):
    for x in range(M):
        if graph[y][x] == 1 and visited[y][x]==0:
            visited[y][x] = -1
    print(' '.join(map(str,visited[y])))