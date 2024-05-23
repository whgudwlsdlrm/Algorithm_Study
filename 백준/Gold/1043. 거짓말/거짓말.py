import sys
from collections import deque
# input = sys.stdin.readline

# (아는 사람 수, 파티 수)
N,M = map(int, input().split())

# 누가 아는 지 (번호는 1~N)
whos = deque(list(map(int, input().split()))[1:])

# 파티 기반 그래프
graph = [[] for _ in range(N+1)]
parties = []
for _ in range(M):
    temp = list(map(int, input().split()))
    parties.append(temp[1:])
    
    for i in range(1, len(temp)):
        adj = temp[1:i] + temp[i+1:]
        graph[temp[i]].extend(adj)

        
# BFS
visited= [False]*(N+1)
while whos:
    que = deque([whos.popleft()])
    
    while que:
      
          node = que.popleft()
          if visited[node]:
              continue

          visited[node] = True
          que.extend(graph[node])

# 파티 계산
count = 0
for party in parties:
    
    honesty = False
    for person in party:
        if visited[person]:
            honesty = True
            break
    
    if not honesty:
        count += 1

print(count)