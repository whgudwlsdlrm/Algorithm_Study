import sys

N = int(sys.stdin.readline())

def check(i, jss, upright, downleft):
  
  result = 0

  if i == N:
    return 1

  for j in range(N):

    if (j not in jss) and ((i+j) not in upright) and ((i-j) not in downleft):
      result += check(i+1, jss+[j], upright+[i+j], downleft+[i-j])

  return result

if N==1:
    print(1)
else:
    print(check(0,[], [],[]))