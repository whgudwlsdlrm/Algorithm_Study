import itertools, sys
input = sys.stdin.readline
# 세울 수 있는 벽의 개수 무조건 3개
# 탐색 + 벽(브루트 포스)

def spread(k,l):
  global graph

  graph[k][l] = 1

  if k>0:
    if graph[k-1][l] == 0:
      spread(k-1,l)
    
  if k<N-1:
    if graph[k+1][l] == 0:
      spread(k+1,l)

  if l>0:
    if graph[k][l-1] == 0:
      spread(k,l-1)
  
  if l<M-1:
    if graph[k][l+1] == 0:
      spread(k,l+1)

N,M = map(int, input().split())

viruses = [] #바이러스
graphs = [] #지도

for i in range(N):

  temp = list(map(int, input().split()))
  graphs.append(temp[:])

  j = 0
  while 2 in temp:
    idx = temp.index(2)
    j += idx+1
    temp = temp[idx+1:]
    viruses.append([i,j-1])
    graphs[i][j-1] = 1

answer = 1e9
for blocks in itertools.combinations([[a,b] for a in range(N) for b in range(M)], 3):

  graph = [temp[:] for temp in graphs]

  turn = True
  for i,j in blocks:
    if graph[i][j] != 0:
      turn = False
      break
    else:
      graph[i][j] = 1

  if turn:
    for virus in viruses:
      spread(virus[0], virus[1])

    answer = min(answer, sum(map(sum, graph)))
  
print(N*M - answer)