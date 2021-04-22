import copy
input_data = []
for _ in range(4):
    input_data.append(list(map(int, input().split())))

board, direction = [], []
for i in range(4):
    temp1, temp2 = [], []
    for j in range(8):
        if j % 2 == 0:
            temp1.append(input_data[i][j])
        else:
            temp2.append(input_data[i][j] - 1)
    board.append(temp1)
    direction.append(temp2)

# 8방향(북, 북서, 서, 남서, 남, 남동, 동, 북동)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

answer = 0
result = []


def pprint(temp):
    for i in range(4):
        for j in range(4):
            print(str(temp[i][j]).rjust(3), end=' ')
        print()
    print()


def shark_possible_move(board, direction, x, y):
    position = []
    shark_dir = direction[x][y]  # 상어 방향
    for i in range(4):
        x += dx[shark_dir]
        y += dy[shark_dir]
        if 0 <= x < 4 and 0 <= y < 4:
            if 0 < board[x][y] <= 16:  # 물고기가 있으면
                position.append((x, y))
    return position


def fish_move(board, direction):
    for fish_number in range(1, 17):  # 번호가 작은 물고기부터 순서대로 이동
        fish_location = []
        for x in range(4):
            for y in range(4):
                if board[x][y] == fish_number:
                    fish_location = [x, y]
        if not len(fish_location):
            continue
        x, y = fish_location  # 물고기 위치
        fish_dir = direction[x][y]  # 물고기 방향
        for i in range(8):
            nx = x + dx[(fish_dir + i) % 8]
            ny = y + dy[(fish_dir + i) % 8]
            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:  # 공간의 경계를 넘을 때
                continue
            if board[nx][ny] == 17:  # 상어가 있을 때
                continue
            # 이동할 수 있는 칸이 있다면 서로 위치 바꾸기
            direction[x][y] = (fish_dir + i) % 8
            board[nx][ny], board[x][y] = board[x][y], board[nx][ny]
            direction[nx][ny], direction[x][y] = direction[x][y], direction[nx][ny]
            break


def dfs(board, direction, x, y, ate_fish_cnt):
    global answer
    board = copy.deepcopy(board)
    direction = copy.deepcopy(direction)
    ate_fish_cnt += board[x][y]
    board[x][y] = 17  # 상어: 17번

    # 물고기 이동
    fish_move(board, direction)

    # 상어 이동
    position = shark_possible_move(board, direction, x, y)
    if not len(position):
        answer = max(answer, ate_fish_cnt)
        return

    for p in position:
        nx, ny = p
        board[x][y] = 0
        dfs(board, direction, nx, ny, ate_fish_cnt)


dfs(board, direction, 0, 0, 0)
print(answer)
