import sys, heapq
input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())

ways = {i:[] for i in range(1,N+1)}
for _ in range(M):
    a, b, cost = map(int,input().split())
    ways[a].append((cost, b))

start, stop = map(int, input().split())
    
que = []
heapq.heappush(que, (0,start))

visited = [False]*(N+1)
while que:
    
    dist,node = heapq.heappop(que)
    
    if node == stop:
        print(dist)
        break
    
    if visited[node]:
        continue
    
    visited[node] = True
    
    for c,n in ways[node]:
        heapq.heappush(que, (dist+c,n))    