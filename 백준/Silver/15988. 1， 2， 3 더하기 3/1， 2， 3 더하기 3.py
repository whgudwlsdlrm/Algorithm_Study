import sys
input = sys.stdin.readline

N = int(input())

nums = [0]*N
for i in range(N):
  nums[i] = int(input())
max_num = max(nums)

array = [0]*max_num
array[0] = 1
array[1] = 2
array[2] = 1 + array[0] + array[1]

for n in range(3,max_num):
  array[n] = (array[n-3] + array[n-2] + array[n-1])%1000000009

for num in nums:
  print(array[num-1]%1000000009)