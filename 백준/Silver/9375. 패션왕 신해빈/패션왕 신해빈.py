import sys
input = sys.stdin.readline

N = int(input())
answers = []
dics = []

for _ in range(N):
  K = int(input())
  dic = {}

  for _ in range(K):
    _, wear = input().split()
    if wear in dic:
      dic[wear] += 1
    else:
      dic[wear] = 1

  dics.append(dic)


for i in range(N):
  temp = 1
  for n in dics[i].values():
    temp *= (n+1)

  answers.append(temp-1)
  
for answer in answers:
  print(answer)