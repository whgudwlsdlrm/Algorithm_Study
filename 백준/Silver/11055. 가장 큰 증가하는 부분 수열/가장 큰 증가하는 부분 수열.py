N = int(input())
A = list(map(int, input().split()))

arrays = [0]*(max(A)+1)
arrays[A[0]] = A[0] # 합,최대 수

for i in range(1,N):
  arrays[A[i]] = max(arrays[:A[i]]) + A[i]

print(max(arrays))