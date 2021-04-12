# 나의 풀이
import sys
from collections import deque

n, l, r = map(int, sys.stdin.readline().rstrip().split())
ground = []
for _ in range(n):
    ground.append(list(map(int, sys.stdin.readline().rstrip().split())))

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# BFS 소스코드 구현
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    visited[x][y] = 1
    sector = [(x, y)]
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == 0 and l <= abs(ground[nx][ny] - ground[x][y]) <= r:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    sector.append((nx, ny))
    union.append(sector)
    # print(union)
    return


answer = 0
while True:
    visited = [[0] * n for _ in range(n)]  # 방문 여부 기록
    union = []
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                bfs(i, j)

    if len(union) == n * n:
        break

    for sec in union:
        population = 0
        for k in range(len(sec)):
            population += ground[sec[k][0]][sec[k][1]]
        for k in range(len(sec)):
            ground[sec[k][0]][sec[k][1]] = population // len(sec)
    answer += 1

print(answer)
