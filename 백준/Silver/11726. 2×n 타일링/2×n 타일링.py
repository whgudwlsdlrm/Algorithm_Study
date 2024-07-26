N = int(input())

array = [0]*max(2,N)

array[0] = 1
array[1] = 2

for n in range(2,N):
  array[n] = array[n-1] + array[n-2]

print(array[N-1]%10007)