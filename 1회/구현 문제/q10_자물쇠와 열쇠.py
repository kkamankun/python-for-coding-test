# 나의 풀이
import copy


def check(n, arr):
    for r in range(n):
        for c in range(n):
            if arr[r + n][c + n] != 1:
                return False
    return True


def rotate_a_matrix_by_90_degree(key):
    m = len(key)
    result = [[0] * m for _ in range(m)]
    for r in range(m):
        for c in range(m):
            result[c][m - 1 - r] = key[r][c]
    return result


def solution(key, lock):
    m, n = len(key), len(lock)
    array = [[0] * 3 * n for _ in range(3 * n)]
    for r in range(n):
        for c in range(n):
            array[r + n][c + n] = lock[r][c]
    ori = copy.deepcopy(array)

    for i in range(4):
        for x in range(2 * n):
            for y in range(2 * n):
                for r in range(m):
                    for c in range(m):
                        array[r + x][c + y] += key[r][c]
                if check(n, array):
                    return True
                else:
                    array = copy.deepcopy(ori)
        key = rotate_a_matrix_by_90_degree(key)
    return False

# 책 풀이
def rotate_a_matrix_by_90_degree(a):
  n = len(a)
  m = len(a)
  result = [[0] * n for _ in range(m)]
  for i in range(n):
    for j in range(m):
      result[j][n - i - 1] = a[i][j]
  return result

def check(new_lock):
  lock_length = len(new_lock) // 3
  for i in range(lock_length, lock_length * 2):
    for j in range(lock_length, lock_length * 2):
      if new_lock[i][j] != 1:
        return False
  return True

def solution(key, lock):
  n = len(lock)
  m = len(key)
  new_lock = [[0] * (n * 3) for _ in range(n * 3)]
  for i in range(n):
    for j in range(n):
      new_lock[i + n][j + n] = lock[i][j]

  for rotation in range(4):
    key = rotate_a_matrix_by_90_degree(key)
    for x in range(n * 2):
      for y in range(n * 2):
        for i in range(m):
          for j in range(m):
            new_lock[x + i][y + j] += key[i][j]
        if check(new_lock) == True:
          return True
        for i in range(m):
          for j in range(m):
            new_lock[x + i][y + j] -= key[i][j]
  return False

print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
