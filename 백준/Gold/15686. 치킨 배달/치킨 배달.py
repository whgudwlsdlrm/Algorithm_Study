import itertools, sys
input = sys.stdin.readline

N,M = map(int, input().split())

graph = []
houses = []
chickens = []

for i in range(N):
  temp = list(map(int, input().split()))
  graph.append(temp)

  idx = 0
  while True:

    if 1 in temp and 2 in temp:
      idx_1 = temp.index(1)
      idx_2 = temp.index(2)

      if idx_1 < idx_2:
        houses.append([i,idx+idx_1])
        temp = temp[idx_1+1:]
        idx += idx_1+1
      else:
        chickens.append([i,idx+idx_2])
        temp = temp[idx_2+1:]
        idx += idx_2+1

    elif 1 in temp:
      idx_1 = temp.index(1)
      houses.append([i,idx+idx_1])
      temp = temp[idx_1+1:]
      idx += idx_1+1

    elif 2 in temp:
      idx_2 = temp.index(2)
      chickens.append([i,idx+idx_2])
      temp = temp[idx_2+1:]
      idx += idx_2+1
    
    else:
      break

distances = []
bests = []
for house in houses:
  distance = []
  for j,chicken in enumerate(chickens):
    distance.append([abs(house[0]-chicken[0]) + abs(house[1]-chicken[1]), j]) #거리,인덱스
  
  distance.sort()
  distances.append(distance[:])

answers = 1e9
cands = list(range(len(chickens)))


for choices in itertools.combinations(cands, r=M):
  
  answer = 0
  for distance in distances:
    
    i = 0
    while distance[i][1] not in choices:
      i += 1
    
    answer += distance[i][0]

  if answers > answer:
    answers = answer

print(answers)