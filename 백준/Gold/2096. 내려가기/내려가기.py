import sys
input = sys.stdin.readline

N = int(input().rstrip())

big = list(map(int, input().split()))
small = big[:]

for _ in range(N-1):
    new_big = list(map(int, input().split()))
    new_small = new_big[:]
    
    for i in range(3):        
        new_big[i] += max(big[max(0,i-1):i+2])
        new_small[i] += min(small[max(0,i-1):i+2])

    big = new_big
    small = new_small

print(max(big), min(small))