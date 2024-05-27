import sys, heapq
input = sys.stdin.readline

N,M,X = list(map(int, input().split()))

back = {i:[] for i in range(N+1)}
go = {i:[] for i in range(N+1)}
for i in range(M):
    start, stop, dist = list(map(int, input().split()))
    go[stop].append((dist, start))
    back[start].append((dist, stop))


# X에서 출발해서 BFS로 각 도시에 도착하면 끝 -> 마지막까지 남는 도시
answer2go = [0]*(N+1)
answer2back = [0]*(N+1)

# go
que = []
heapq.heappush(que, (0,X))
visited = [False]*(N+1)

while que:
    dist1, city = heapq.heappop(que)

    if visited[city]:
        continue
    answer2go[city] = dist1
    visited[city] = True
    
    for d,c in go[city]:
          heapq.heappush(que, (dist1+d, c))


# back
que = []
heapq.heappush(que, (0,X))
visited = [False]*(N+1)

while que:
    dist2, city = heapq.heappop(que)

    if visited[city]:
      continue

    answer2back[city] = dist2
    visited[city] = True
    
    for d,c in back[city]:
          heapq.heappush(que, (dist2+d, c))


# shortest
answer = 0
for g,b in zip(answer2go, answer2back):

  temp = g+b
  if answer < temp:
    answer = temp

print(answer)