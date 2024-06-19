# DFS, 백트래킹

import sys
import heapq
input = sys.stdin.readline

# 멀리 떨어져있는 노드도 셀 수 있구나!
# 직원 i의 상사 번호는 i보다 작거나 같은 음이 아닌 정수

# 아래에 딸려있는 서브트리의 크기에 따라 너무 많이 달라지는데
# 아래에서 부터 쌓아올려야 하나?


N = int(input())
parents = list(map(int, input().split()))

tree = [ [] for _ in range(N) ]
childs = [ 0 for _ in range(N) ]

for child, parent in enumerate(parents):
    if parent == -1: continue
    tree[parent].append(child)

def check(node):
    
    if len(tree[node]) == 0:
        return 0

    temp = []
    for child in tree[node]:
        heapq.heappush(temp, -1*check(child))

    result = []
    for i in range(len(temp)):
        time = heapq.heappop(temp)
        result.append(-1*time + i + 1)

    return max(result)

print(check(0))