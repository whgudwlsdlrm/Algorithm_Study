n = int(input())
array = list(map(int, input().split()))

right = [0]*n
result = [0]*n

min_ = 0
for i in range(n):
  if i == 0:
    right[i] = array[i]
    result[i] = array[i]
  else:
    right[i] = right[i-1] + array[i]
    result[i] = right[i] - min_
  if min_ > right[i]:
    min_ = right[i]

print(max(result))