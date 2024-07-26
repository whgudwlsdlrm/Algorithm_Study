N = int(input())

array = [0] * max(3,abs(N)+1)
array[0] = 0
array[1] = 1

for n in range(2,abs(N)+1):
    array[n] = (array[n-2] + array[n-1])%1000000000

if N < 0:
  new_N = N*-1
  if new_N % 2 == 0:
    print(-1)
  else:
    print(1)
  print(array[new_N])

else:
  if array[N] == 0:
    print(0)
  else:
    print(1)
  print(array[N])