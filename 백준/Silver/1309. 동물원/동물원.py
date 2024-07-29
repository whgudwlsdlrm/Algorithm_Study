N = int(input())

left = 1
right = 1
no = 1

for n in range(1,N):
  new_left = left + no
  new_right = right + no
  new_no = left + right + no

  left = new_left
  right = new_right
  no = new_no

print((left+right+no)%9901)