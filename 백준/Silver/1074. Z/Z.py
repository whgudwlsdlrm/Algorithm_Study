N,r,c = map(int, input().split())
r,c = r+1,c+1

def check(r,c,N): # N단위에서 한 단위 씩 아래로 내릴 때

  if r <= 2**(N-1):
    if c <= 2**(N-1):
        i,j,k = 0,0,0
    else:
        i,j,k = 0,1,1

  else:
    if c <= 2**(N-1):
        i,j,k = 1,0,2
    else:
        i,j,k = 1,1,3
  
  r -= 2**(N-1)*i
  c -= 2**(N-1)*j

  return r,c,2**(2*(N-1))*(k)


total = 0
for n in range(N,0,-1):
    # print(f'\n\n{n},{r},{c}')
    r,c,count = check(r,c,n)
    # print(count)
    total += count
  
    if (r,c) == (1,1): break

print(total)