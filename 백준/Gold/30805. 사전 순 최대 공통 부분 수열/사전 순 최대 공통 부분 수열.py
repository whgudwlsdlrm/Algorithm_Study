import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))

# 어차피 앞쪽에서 시작 수에서 다 판명나
# 힙큐로 가자

result = []
while A and B:
  temp = max(A)
  if temp in B:
    idx_A = A.index(temp)
    idx_B = B.index(temp)

    A = A[idx_A+1:]
    B = B[idx_B+1:]

    result.append(temp)

  else:
    idx_A = A.index(temp)
    A.pop(idx_A)

if result:
  print(len(result))
  print(' '.join(map(str, result)))
else:
    print(len(result))