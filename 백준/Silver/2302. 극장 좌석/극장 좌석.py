import sys
input = sys.stdin.readline

N = int(input()) # 1~40
M = int(input()) # 0~N

# change: 앞사람이랑 바꾼 경우

seats = [0]*(N+1)
for _ in range(M):
  seats[int(input())] = 1

change,no = 0,1

for n in range(2,N+1):

  if seats[n] == 1:
    change, no = 0, no+change

  elif seats[n-1] == 1:
    change, no = 0, no+change

  else:
    change, no = no, no+change

print(change + no)