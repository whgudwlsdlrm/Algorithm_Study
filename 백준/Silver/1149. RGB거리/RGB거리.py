# 인접한 집끼리는 색이 달라야 한다

import sys, heapq
input = sys.stdin.readline

N = int(input())

cost = []
for _ in range(N):
  cost.append(list(map(int, input().split())))

for i in range(1,N):
    
    temp = []
    for h,t in enumerate(cost[i-1]):
      heapq.heappush(temp, (t,h))
    
    first,idx1 = heapq.heappop(temp)

    for j in range(3):
        if idx1 == j:
            continue    
        cost[i][j] += cost[i-1][idx1]
    
    second,_ = heapq.heappop(temp)
    cost[i][idx1] += second

print(min(cost[N-1]))