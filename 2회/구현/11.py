from collections import deque

n = int(input())
k = int(input())
apple = []
for _ in range(k):
    apple.append(list(map(int, input().split())))
L = int(input())
info = [0] * 10001
for _ in range(L):
    X, C = input().split()
    info[int(X)] = C

board = [[0] * n for _ in range(n)]
for a in apple:
    x, y = a
    board[x - 1][y - 1] = 1
board[0][0] = 2

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
t = 0
i = 0
snake = deque()
snake.append((0, 0))
while True:
    t += 1
    head_x, head_y = snake[-1]
    nx = head_x + dx[i]
    ny = head_y + dy[i]
    if nx < 0 or nx >= n or ny < 0 or ny >= n:  # 벽에 부딪힘
        break
    if board[nx][ny] == 2:  # 자기자신의 몸과 부딪힘
        break
    if board[nx][ny] == 1:  # 사과가 있다면
        board[nx][ny] = 2
        snake.append((nx, ny))
    else:  # 사과가 없다면
        board[nx][ny] = 2
        snake.append((nx, ny))
        tail_x, tail_y = snake.popleft()
        board[tail_x][tail_y] = 0
    if info[t] != 0:
        rotate = info[t]
        if rotate == 'D':
            i += 1
        else:
            i -= 1
        if i == 4:
            i = 0
        if i == -1:
            i = 3

answer = t
print(answer)
