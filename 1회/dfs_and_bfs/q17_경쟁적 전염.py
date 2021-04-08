# 나의 풀이
from collections import deque

n, k = map(int, input().split())
graph = []
temp = list()
for r in range(n):
    graph.append(list(map(int, input().split())))
    for c in range(n):
        if graph[r][c] > 0:
            temp.append((graph[r][c], r, c))
s, X, Y = map(int, input().split())

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

temp.sort()
queue = deque(temp)
t = 0
while queue:
    v, x, y = queue.popleft()
    if queue:
        next_v = queue[0][0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            # 해당 위치에 바이러스가 존재하지 않는다면 증식
            if graph[nx][ny] == 0:
                graph[nx][ny] = v
                queue.append((v, nx, ny))
    if v == k and next_v == 1:
        t += 1
    if t == s:
        break
print(graph[X - 1][Y - 1])
