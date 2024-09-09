import sys
input = sys.stdin.readline

def check(x,y):

  global visited,explodes,backs

  # 진입할 필요도 X
  if visited[x][y]:
    return

  visited[x][y] = True
  backs[x] += [y]  

  if y>0:
    if graphs[x][y-1] == graphs[x][y]:
      check(x,y-1)
  if y<11:
    if graphs[x][y+1] == graphs[x][y]:
      check(x,y+1)
  if x>0:
    if graphs[x-1][y] == graphs[x][y]:
      check(x-1,y)
  if x<5:
    if graphs[x+1][y] == graphs[x][y]:
      check(x+1,y)
    
# 입력
graphs = []
for _ in range(12):
  graphs.append(input().strip())
graphs = list(map(list, zip(*graphs)))

visited = [[False]*12 for _ in range(6)] #방문
explodes = [[] for _ in range(6)] #폭발

t = 0
while True: #1초마다

  # 탐색
  for i in range(12):
    for j in range(6):

      if graphs[j][i] != '.' and not visited[j][i]:
        backs = [[] for _ in range(6)]
        check(j,i)
        if sum(map(len, backs))>=4:
          for k in range(6):
            explodes[k] += backs[k]

  # 검사
  if sum(map(len, explodes)) == 0:
    break
  else:
    # 폭발
    for x in range(6):
      if explodes[x]:        
        explodes[x] = [-1]+sorted(explodes[x])+[12]
        
        temp = []
        for k in range(1, len(explodes[x])):
          temp += graphs[x][explodes[x][k-1]+1:explodes[x][k]]
        graphs[x] = ['.']*(12-len(temp))+temp
    
    # 다음 초를 위한 초기화
    t += 1
    explodes = [[] for _ in range(6)]
    visited = [[False]*12 for _ in range(6)]

print(t)