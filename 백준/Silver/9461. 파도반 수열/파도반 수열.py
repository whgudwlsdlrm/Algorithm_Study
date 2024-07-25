import sys
input = sys.stdin.readline

T = int(input())

Ns = []
for _ in range(T):
  Ns.append(int(input()))

lengths = [1]*101
lengths[0] = 0
lengths[4] = 2
lengths[5] = 2

for i in range(6,max(Ns)+1):
  lengths[i] = lengths[i-1] + lengths[i-5]

for N in Ns:
  print(lengths[N])