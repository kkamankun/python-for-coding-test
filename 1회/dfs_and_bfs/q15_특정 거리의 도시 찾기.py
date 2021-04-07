# 나의 풀이
from collections import deque
import sys

n, m, k, x = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    # graph[b].append(a)

queue = deque()
dist = [-1] * (n + 1)
queue.append(x)
dist[x] = 0
while queue:
    now = queue.popleft()
    for i in graph[now]:
        if dist[i] == -1:
            dist[i] = dist[now] + 1
            queue.append(i)

for i in range(n + 1):
    if dist[i] == k:
        print(i)
if k not in dist:
    print(-1)
