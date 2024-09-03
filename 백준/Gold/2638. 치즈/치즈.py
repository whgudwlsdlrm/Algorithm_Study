import sys
input = sys.stdin.readline

def inandout(i,j):

  global visited, airs, cands

  que = deque([])
  que.append((i,j))

  while que:
    
    i,j = que.popleft()
    if visited[i][j] == 1:
      continue

    if graphs[i][j] == 0:
      airs[i][j] = 0
      visited[i][j] = 1
      if i > 0:
        que.append((i-1,j))
      if i < N-1:
        que.append((i+1,j))
      if j > 0:
        que.append((i,j-1))
      if j < M-1:
        que.append((i,j+1))

    elif airs[i-1][j] + airs[i+1][j] + airs[i][j-1] + airs[i][j+1] < 3:
      visited[i][j] = 1
      cands.append((i,j))
      continue


def update(i,j):

  global airs, visited

  que = deque([])
  que.append((i,j))
  visited[i][j] = 0
  
  new_cands = []

  while que:

    i,j = que.popleft()
    if visited[i][j] == 1: #온 적 있으면
      pass

    elif graphs[i][j] == 0: #치즈X
      visited[i][j] = 1
      airs[i][j] = 0
      if i > 0:
        que.append((i-1,j))
      if i < N-1:
        que.append((i+1,j))
      if j > 0:
        que.append((i,j-1))
      if j < M-1:
        que.append((i,j+1))

    elif airs[i-1][j] + airs[i+1][j] + airs[i][j-1] + airs[i][j+1] < 3: # 내부&치즈&인접
      visited[i][j] = 1
      new_cands.append((i,j))
    
  return new_cands


from collections import deque

N,M = map(int, input().split())

graphs = [list(map(int, input().split())) for _ in range(N)]
airs = [[1]*M for _ in range(N)]
cands = []

# 네 가장자리에서 쭉 탐색
visited = [[0]*M for _ in range(N)]
for i,j in [(0,0), (0,M-1), (N-1,0), (N-1,M-1)]:
  inandout(i,j)

# time
time = 0
while cands:
  for i,j in cands:
    graphs[i][j] = 0

  new_cands = []
  for i,j in cands:
    new_cands += update(i,j)

  cands = new_cands[:]
  time += 1

print(time)