N = int(input())
A = list(map(int, input().split()))

dp = [0]*(max(A)+1)
for i in range(len(A)):
  dp[A[i]] = max(dp[:A[i]]) + 1

print(max(dp))