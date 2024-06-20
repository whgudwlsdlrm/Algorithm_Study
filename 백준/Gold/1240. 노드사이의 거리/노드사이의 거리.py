import sys,heapq
input = sys.stdin.readline

# 트리에서 노드 사이의 거리 구하기

N,M = map(int, input().split())

tree = { i:[] for i in range(1,N+1)}
for _ in range(N-1):
    node1, node2, dist = map(int, input().split())
    tree[node1].append([dist, node2])
    tree[node2].append([dist, node1])

questions = []
for _ in range(M):
    questions.append(list(map(int, input().split())))

for start, stop in questions:
    
    visited = [False]*(N+1)
    que = [(0,start)]
    while que:
        
        dist, node = heapq.heappop(que)
        if node == stop:
            print(dist)
            break
        
        if visited[node]:
            continue
            
        visited[node] = True
        for info in tree[node]:
            heapq.heappush(que, (info[0]+dist, info[1]))