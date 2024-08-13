import sys
input = sys.stdin.readline

H,W = map(int, input().split())
Ws = list(map(int, input().split()))

# 1) W별 H -> H별 W
Hs = [[] for _ in range(H+1)]
for h in range(H+1):
  for w in range(len(Ws)):
    if Ws[w] >= h:
      Hs[h].append(w)

# 2) H별 scanning
waters = 0
for h in Hs:
  if len(h)>1:
    waters += (h[-1]-h[0]-1) - len(h)+2

print(waters)