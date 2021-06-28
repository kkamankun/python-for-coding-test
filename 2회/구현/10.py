def rotate_a_matrix_by_90_degree(a):
    row_length = len(a)
    column_length = len(a[0])
    result = [[0] * row_length for _ in range(column_length)]
    for r in range(row_length):
        for c in range(column_length):
            result[c][row_length - 1 - r] = a[r][c]
    return result


def is_unlock(n, board):
    cnt = 0
    for i in range(n, 2 * n):
        for j in range(n, 2 * n):
            if board[i][j] == 1:
                cnt += 1
    if cnt == n * n:
        return True
    else:
        return False


def solution(key, lock):
    answer = False
    m = len(key)
    n = len(lock)
    board = [[0] * (n * 3) for _ in range(n * 3)]
    for i in range(n):
        for j in range(n):
            board[i + n][j + n] = lock[i][j]

    for rotate in range(4):
        for x in range(n + m - 1):
            for y in range(n + m - 1):
                for i in range(m):
                    for j in range(m):
                        board[n - m + 1 + i + x][n - m + 1 + j + y] += key[i][j]
                if is_unlock(n, board):
                    answer = True
                for i in range(m):
                    for j in range(m):
                        board[n - m + 1 + i + x][n - m + 1 + j + y] -= key[i][j]
        key = rotate_a_matrix_by_90_degree(key)

    return answer


# print(solution([[0, 0, 0], [0, 0, 1], [0, 1, 0]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))