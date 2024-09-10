import sys
from collections import deque
input = sys.stdin.readline


N = int(input())

shark_pos = []
graphs = []
for i in range(N):
  temp = list(map(int, input().split()))
  graphs.append(temp[:])

  if 9 in temp:
    count,shark,shark_pos = 2,2,[i,temp.index(9)]
    graphs[shark_pos[0]][shark_pos[1]] = 0


answer,t,found = 0,-1,[]
visited = [[False]*N for _ in range(N)]
que = deque([shark_pos])
new_que  = deque([])


while que:  

  # 초마다 BFS
  t += 1
  while que:

    i,j = que.popleft()

    if visited[i][j]:
      continue
    visited[i][j] = True

    if graphs[i][j] > shark:
      continue
    elif 0 < graphs[i][j] < shark:
      found.append([i,j])
    else:
      if i>0:
        new_que.append([i-1,j])
      if j>0:
        new_que.append([i,j-1])
      if j<N-1:
        new_que.append([i,j+1])
      if i<N-1:
        new_que.append([i+1,j])


  # 찾았으면 초기화
  if found:

    y,x = min(found)
    graphs[y][x] = 0
    found = []

    answer += t
    count -= 1
    if count == 0:
      shark += 1
      count = shark
    
    t = -1
    visited = [[False]*N for _ in range(N)]
    que, new_que = deque([[y,x]]), deque([])
    

  # 못찾았으면 계속 탐색
  else:
    que, new_que = new_que, deque([])

print(answer)