N = int(input())

array = [-1]*5010
array[3] = 1
array[5] = 1

for weight in range(1,N+1-3):
  if array[weight] != -1:

    if array[weight+3] == -1:
      array[weight + 3] = array[weight]+1
    else:
      array[weight + 3] = min(array[weight+3], array[weight]+1)
    
    if array[weight+5] == -1:
      array[weight + 5] = array[weight]+1
    else:
      array[weight + 5] = min(array[weight+5], array[weight]+1)

print(array[N])