import sys, heapq
input = sys.stdin.readline

N = int(input().rstrip())
que = []

for _ in range(N):
    temp = int(input().rstrip())
    
    if temp == 0:
        if que:
            print(heapq.heappop(que)[1])
        else:
            print(0)
    else:
        heapq.heappush(que, (abs(temp), temp))
