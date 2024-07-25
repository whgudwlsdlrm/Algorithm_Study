import sys
input = sys.stdin.readline

N = int(input())

steps = []
for _ in range(N):
  steps.append(int(input()))


block = [0]*N
non_block = [0]*N

block[0] = 0
non_block[0] = steps[0]



for n in range(1,N):

  if n==1:
    block[n] = steps[n-1]
    non_block[n] = steps[n-1] + steps[n]
  
  elif n==2:
    block[n] = steps[n-1] + steps[n-2]
    non_block[n] = max(steps[n-1],steps[n-2]) + steps[n]
  
  else:
    non_block[n] = max(block[n-2]+steps[n-1], non_block[n-2]) + steps[n]
    block[n] = max(block[n-3] + steps[n-2] + steps[n-1], block[n-2]+steps[n-1])

print(non_block[N-1])