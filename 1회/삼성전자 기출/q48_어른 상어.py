def update():
    for x in range(n):
        for y in range(n):
            if timer[x][y] > 0:
                timer[x][y] -= 1
                if timer[x][y] == 0:
                    smell[x][y] = 0
            if shark[x][y] > 0:
                smell[x][y] = shark[x][y]
                timer[x][y] = k


def check():
    cnt = 0
    for x in range(n):
        for y in range(n):
            if shark[x][y] > 0:
                cnt += 1
    if cnt == 1:
        return True
    else:
        return False


def move():
    dx = [0, -1, 1, 0, 0]
    dy = [0, 0, 0, -1, 1]

    shark_pos = []
    for x in range(n):
        for y in range(n):
            if shark[x][y] != 0:
                shark_pos.append((x, y))

    for s_pos in shark_pos:
        x, y = s_pos
        direction = directions[shark[x][y]]
        priority = priorities[shark[x][y]][direction]

        found = False
        # 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 이동 방향 결정
        for d in priority:
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if smell[nx][ny] > 0:
                continue
            if smell[nx][ny] == 0:
                directions[shark[x][y]] = d
                if shark[nx][ny] != 0:
                    shark[nx][ny] = min(shark[nx][ny], shark[x][y])
                else:
                    shark[nx][ny] = shark[x][y]
                shark[x][y] = 0
                found = True
                break

        # 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 이동 방향 결정
        if not found:
            for d in priority:
                nx = x + dx[d]
                ny = y + dy[d]
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    continue
                # 자신의 냄새가 있는 칸으로 이동
                if smell[nx][ny] == shark[x][y]:
                    directions[shark[x][y]] = d
                    shark[nx][ny] = shark[x][y]
                    shark[x][y] = 0
                    break
    return


n, m, k = map(int, input().split())
timer = [[0] * n for _ in range(n)]
smell = [[0] * n for _ in range(n)]
shark = []
for i in range(n):
    shark.append(list(map(int, input().split())))
directions = [0] + list(map(int, input().split()))
priorities = [0]
for i in range(m):
    temp = [0]
    for _ in range(4):
        temp.append(list(map(int, input().split())))
    priorities.append(temp)

time = 0
while True:
    update()
    time += 1
    move()

    if check():
        print(time)
        break

    if time >= 1000:
        print(-1)
        break
