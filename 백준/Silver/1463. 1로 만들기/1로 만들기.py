import heapq

N = int(input())

nums = [(0,N)]
visited = []
while True:
    count, num = heapq.heappop(nums)

    if num == 1:
        print(count)
        break

    if num % 3 ==0:
        new = num//3
        if new not in visited:    
            heapq.heappush(nums, (count+1, new))
            visited.append(new)
        
    if num % 2 ==0:
        new = num//2
        if new not in visited:       
            heapq.heappush(nums, (count+1, new))
            visited.append(new)

    new = num-1
    if new not in visited:
        heapq.heappush(nums, (count+1, new))