# 파이프 오른쪽으러 밀기: 수평, 대각선, 수직

# 45도 회전
# 수평: 우측 칸 유지
# 대각선: 우측아래 칸 유지
# 수직: 아래 칸 유지

# (1,1),(1,2) -> (N,N)
# 0:뚫 / 1:벽
# 한쪽 끝을 N,N으로 "이동시키는 방법의 수"에 대해서 알아보자
# DP: "우하단" 끝이 어디 있는가를 기준으로
import sys
input = sys.stdin.readline

N = int(input())

vert,hor,cross = [],[],[]
for _ in range(N):
  temp = list(map(int, input().split()))
  while 1 in temp:
    temp[temp.index(1)] = -1
  vert.append(temp[:])
  hor.append(temp[:])
  cross.append(temp[:])


# 가로 파이프 밀기
def horizontal(i,j):
  global hor, vert, cross

  if j < N-1:
    if hor[i][j+1] != -1:
      hor[i][j+1] += hor[i][j]

  if j < N-1 and i < N-1:
    if hor[i+1][j+1] != -1 and hor[i][j+1] != -1 and hor[i+1][j] != -1:
      cross[i+1][j+1] += hor[i][j]

# 세로 파이프 밀기
def vertical(i,j):
  global hor, vert, cross

  if i < N-1:
    if vert[i+1][j] != -1:
      vert[i+1][j] += vert[i][j]
  
  if i < N-1 and j < N-1:
    if vert[i+1][j+1] != -1 and vert[i+1][j] != -1  and vert[i][j+1] != -1:
      cross[i+1][j+1] += vert[i][j]

# 대각선 파이프 밀기
def across(i,j):
  global hor, vert, cross

  if j < N-1:
    if hor[i][j+1] != -1:
      hor[i][j+1] += cross[i][j]
  
  if i < N-1:
    if vert[i+1][j] != -1:
      vert[i+1][j] += cross[i][j]
  
  if i< N-1 and j < N-1:
    if cross[i+1][j+1] != -1  and hor[i][j+1] != -1 and hor[i+1][j] != -1:
      cross[i+1][j+1] += cross[i][j]

# 파이프 밀기 종합
def dp(i,j):
  horizontal(i,j)
  vertical(i,j)
  across(i,j)

# 초기값
hor[0][1] = 1

#
for total in range(1,N):
  
  for k in range(total):

    if hor[total][k] != -1:
      dp(total, k)
    if hor[k][total] != -1:
      dp(k, total)

  if hor[total][total] != -1:
    dp(total, total)


print(max(0,hor[N-1][N-1])+max(0,vert[N-1][N-1])+max(0,cross[N-1][N-1]))