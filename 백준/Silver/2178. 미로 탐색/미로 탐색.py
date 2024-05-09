import sys
from collections import deque

input = sys.stdin.readline

N,M = list(map(int, input().split()))
goal = (M-1,N-1)

graph = []
visited = [[0]*M for _ in range(N)]

for _ in range(N):
    graph.append(list(map(int, input().rstrip())))
    
que = deque([(1,(0,0))])

while True:
    d,(x,y) = que.popleft()
    
    if (x,y)==goal:
        print(d)
        break
    
    if visited[y][x]==1:
        continue
    else:
      visited[y][x] = 1
    
    if y<(N-1):
      if graph[y+1][x]==1:
        que.append((d+1,(x,y+1)))
    if 0<y:
      if graph[y-1][x]==1:
        que.append((d+1,(x,y-1)))
    if 0<x:
      if graph[y][x-1]==1:
        que.append((d+1,(x-1,y)))
    if x<(M-1):
      if graph[y][x+1]==1:
        que.append((d+1,(x+1,y)))