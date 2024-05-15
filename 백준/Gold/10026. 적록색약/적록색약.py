# 상하좌우 같은 색 인접구역
# RGB

# BFS로

import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
graphs = [ list(input()) for _ in range(N) ]
visited = [[0]*N for _ in range(N)]
start = deque([])
que = deque([])
start.append((0,0))

RG = {'R':1, 'G':1, 'B':0}

count = 0
while start:
    
    temp = start.popleft()
    if visited[temp[0]][temp[1]] == 0:
      que.append(temp)
      count += 1
      while que:
          x,y = que.popleft()
      
          if visited[x][y]==1:
              continue
          
          visited[x][y] = 1
          
          if 0<x:
              if graphs[x][y] == graphs[x-1][y]:
                  que.append((x-1,y))
              else:
                  start.append((x-1,y))
      
          if x<(N-1):
              if graphs[x][y] == graphs[x+1][y]:
                  que.append((x+1,y))
              else:
                  start.append((x+1,y))
      
      
          if 0<y:
              if graphs[x][y-1] == graphs[x][y]:
                  que.append((x,y-1))
              else:
                  start.append((x,y-1))
      
          if y<(N-1):
              if graphs[x][y] == graphs[x][y+1]:
                  que.append((x,y+1))
              else:
                  start.append((x,y+1))

answer = [count]
start.append((0,0))
visited = [[0]*N for _ in range(N)]
count = 0
while start:
    
    temp = start.popleft()
    if visited[temp[0]][temp[1]] == 0:
      que.append(temp)
      count += 1
      while que:
          x,y = que.popleft()
      
          if visited[x][y]==1:
              continue
          
          visited[x][y] = 1
          
          if 0<x:
              if RG[graphs[x][y]] == RG[graphs[x-1][y]]:
                  que.append((x-1,y))
              else:
                  start.append((x-1,y))
      
          if x<(N-1):
              if RG[graphs[x][y]] == RG[graphs[x+1][y]]:
                  que.append((x+1,y))
              else:
                  start.append((x+1,y))
      
      
          if 0<y:
              if RG[graphs[x][y-1]] == RG[graphs[x][y]]:
                  que.append((x,y-1))
              else:
                  start.append((x,y-1))
      
          if y<(N-1):
              if RG[graphs[x][y]] == RG[graphs[x][y+1]]:
                  que.append((x,y+1))
              else:
                  start.append((x,y+1))

answer.append(count)
print(answer[0], answer[1])