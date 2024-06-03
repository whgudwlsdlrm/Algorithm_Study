import sys
input = sys.stdin.readline

# recursion
N = int(input())

tree = {}

for _ in range(N):
    temp = input().split()
    tree[temp[0]] = temp[1:]

def search(node):
    global pre_ans, in_ans, post_ans 
    
    pre_ans += node
    
    if tree[node][0] != '.':
        search(tree[node][0])
    
    in_ans += node
        
    if tree[node][1] != '.':
        search(tree[node][1])
    
    post_ans += node

pre_ans, in_ans, post_ans = '','',''
search('A')

print(pre_ans)
print(in_ans)
print(post_ans)