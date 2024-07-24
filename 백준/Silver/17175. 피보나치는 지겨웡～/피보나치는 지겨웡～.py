N = int(input())

array = [0]*52

array[0] = 0
array[1] = 0
array[2] = 2 + array[1] + array[0]
array[3] = 2 + array[2] + array[1]

for n in range(4, N+1):
  array[n] = 2 + array[n-1] + array[n-2]

print((array[N]+1)%1000000007)