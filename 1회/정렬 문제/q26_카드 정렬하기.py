from queue import PriorityQueue
que = PriorityQueue()
n = int(input())
for i in range(n):
    que.put(int(input()))

cnt = []
for i in range(n-1):
    s = que.get() + que.get()
    cnt.append(s)
    que.put(s)

print(sum(cnt))
