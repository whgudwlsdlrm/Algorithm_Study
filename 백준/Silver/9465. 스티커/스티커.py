import sys
# input = sys.stdin.readline

N = int(input())
stickers = [[] for _ in range(N)]

for i in range(N):
    n = int(input())
    stickers[i].append(list(map(int, input().split())))
    stickers[i].append(list(map(int, input().split())))

for t in range(N):

    n = len(stickers[t][0])
    result = [[] for _ in range(n)]

    sticker = stickers[t]
    result[0] = sticker[0][0], sticker[1][0], 0

    for i in range(1,n):
        result[i] = max(result[i-1][1],result[i-1][2])+sticker[0][i], max(result[i-1][0],result[i-1][2])+sticker[1][i], max(result[i-1][0], result[i-1][1])

    print(max(result[-1]))