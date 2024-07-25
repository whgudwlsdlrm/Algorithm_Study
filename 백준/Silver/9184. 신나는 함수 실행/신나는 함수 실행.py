import sys
input = sys.stdin.readline

array = [[[1]*21 for _ in range(21)] for _ in range(21)]

for i in range(1,21):
  for j in range(1,21):
    for k in range(1,21):
      if i<j and j<k:
        array[i][j][k] = array[i][j][k-1] + array[i][j-1][k-1] - array[i][j-1][k]
      else:
        array[i][j][k] = array[i-1][j][k] + array[i-1][j-1][k] + array[i-1][j][k-1] - array[i-1][j-1][k-1]

graphs = []
while True:
  temp = list(map(int, input().split()))
  if temp == [-1,-1,-1]:
    break
  graphs.append(temp)

for a,b,c in graphs:
  print(f'w({a}, {b}, {c}) = ', end='')
  if a<=0 or b<=0 or c<=0:
    print(1)
  elif a>20 or b>20 or c>20:
    print(array[20][20][20])
  else:
    print(array[a][b][c])