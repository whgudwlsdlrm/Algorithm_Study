import sys
input = sys.stdin.readline

N = int(input())
array = [0]*N

array[0] = 1

for i in range(1,N):
  if i == 1:
    array[i] = 2
  else:
    array[i] = (array[i-1] + array[i-2])%15746

print(array[N-1])