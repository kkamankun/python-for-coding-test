from collections import deque
import sys
n = int(sys.stdin.readline().rstrip())  # 보드의 크기 n * n
board = []
visited = [[0] * n for _ in range(n)]
shark_pos = [0, 0]
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().rstrip().split())))
    for j in range(n):
        if board[i][j] == 9:
            shark_pos = [i, j]  # 아기 상어 위치
            visited[i][j] = 1

shark_size = 2
fish_cnt = 0
time = 0

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()

while True:
    q.append(shark_pos)
    candidate = []
    distance = 0
    while q:
        x, y = q.popleft()
        distance += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if board[nx][ny] > shark_size:  # 장애물(더 큰 물고기)가 있으면
                continue
            if not visited[nx][ny]:
                q.append((nx, ny))
                visited[nx][ny] = visited[x][y] + 1
                if 0 < board[nx][ny] < shark_size:  # 상어보다 작은 물고기가 있다면
                    candidate.append((visited[nx][ny] - 1, nx, ny))  # 물고기까지의 거리와 물고기의 위치 저장
    if not len(candidate):
        break

    candidate.sort()
    # 아기 상어 이동
    nearest = candidate[0]
    time += nearest[0]
    board[shark_pos[0]][shark_pos[1]] = 0  # 아기 상어가 있던 곳
    board[nearest[1]][nearest[2]] = 9
    shark_pos = [nearest[1], nearest[2]]
    visited = [[0] * n for _ in range(n)]
    visited[shark_pos[0]][shark_pos[1]] = 1
    fish_cnt += 1
    if fish_cnt == shark_size:
        shark_size += 1
        fish_cnt = 0

print(time)
