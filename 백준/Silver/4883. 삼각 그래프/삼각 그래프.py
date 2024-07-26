import sys
input = sys.stdin.readline

answers = []

while True:

  N = int(input())
  if N == 0:
    break

  graph = []
  for _ in range(N):
    graph.append(list(map(int, input().split())))
  graph[0][2] = graph[0][1] + graph[0][2]

  for h in range(1,N):
    if h==1:
        graph[h][0] += graph[h-1][1]
        graph[h][1] += min(graph[h-1][1], graph[h-1][2], graph[h][0])
    else:
        graph[h][0] += min(graph[h-1][0], graph[h-1][1])
        graph[h][1] += min(graph[h-1][0], graph[h-1][1], graph[h-1][2], graph[h][0])
        
    graph[h][2] += min(graph[h-1][1], graph[h-1][2], graph[h][1])

  answers.append(graph[N-1][1])

for i,answer in enumerate(answers):
  print(f"{i+1}. {answer}")