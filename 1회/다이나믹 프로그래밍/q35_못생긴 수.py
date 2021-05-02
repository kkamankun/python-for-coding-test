import heapq
# n번째 못생긴 수를 구하라
n = int(input())
h = [1]
cnt = 0
prev = 0
while True:
    ugly = heapq.heappop(h)
    if prev == ugly:
        continue
    cnt += 1
    heapq.heappush(h, ugly * 2)
    heapq.heappush(h, ugly * 3)
    heapq.heappush(h, ugly * 5)
    prev = ugly
    if cnt == n:
        break
print(ugly)
