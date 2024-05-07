N = int(input())
M = int(input())

S = input()
word = 'I'+'OI'*N


i,count = 0,0
while i <= len(S)-len(word):
  if S[i] == 'I':
    if S[i:i+len(word)] == word:
      count += 1
      i += 2
    else:
      i += 1
  else:
    i += 1

print(count)
