import sys, heapq
input = sys.stdin.readline

V,E = map(int, input().split())
start = int(input().rstrip())

graph = {i:[] for i in range(1,V+1)}
for _ in range(E):
    u,v,w = map(int, input().split())    
    graph[u].append((w,v)) # 거리,노드

que = []
heapq.heappush(que, (0,start))
visited = [False]*(V+1)

distance = [1e9]*(V+1)

while que:
    
    dist,node = heapq.heappop(que)
    if visited[node]:
        continue
    
    visited[node] = True
    distance[node] = dist
    
    for d,n in graph[node]:
        heapq.heappush(que, (dist+d,n))
    
for i in range(1,V+1):
    
    if distance[i]==1e9:
        print('INF')
    else:
        print(distance[i])