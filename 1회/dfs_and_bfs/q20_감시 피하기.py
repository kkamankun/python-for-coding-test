# 나의 풀이
from collections import deque
import itertools
import copy
import pprint

# N 입력받기
n = int(input())
# 2차원 리스트의 맵 정보 입력받기
graph_ori = []
for i in range(n):
    graph_ori.append(list(input().split()))
graph_test = copy.deepcopy(graph_ori)

# 이동할 네 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 2차원 리스트에서 값이 X인 요소들의 위치 찾기
list_X = [[i, j] for i in range(n) for j in range(n) if graph_ori[i][j] == 'X']

# 2차원 리스트에서 값이 T인 요소들의 위치 찾기
list_T = [[i, j] for i in range(n) for j in range(n) if graph_ori[i][j] == 'T']


# BFS 소스코드 구현
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x, y))
    tx, ty = x, y
    # 큐가 빌 때까지 반복
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 복도를 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if nx == tx or ny == ty:
                # 장애물이면 무시
                if graph_test[nx][ny] == 'O':
                    continue
                # 학생인 경우 탐색 종료
                if graph_test[nx][ny] == 'S':
                    # print('학생: ', nx, ny)
                    return False
                # 선생님이 볼 수 있는 영역으로 기록
                if graph_test[nx][ny] == 'X':
                    graph_test[nx][ny] = 'T'
                    queue.append((nx, ny))
                    # print(nx, ny)
    return True


answer = ''
# 장애물 3개를 세울 수 있는 조합
for x in itertools.combinations(list_X, 3):
    possible = 1

    # 선생님 퍼트리기(BFS)
    for y in list_T:
        graph_test[x[0][0]][x[0][1]] = 'O'  # 장애물 세우기1
        graph_test[x[1][0]][x[1][1]] = 'O'  # 장애물 세우기2
        graph_test[x[2][0]][x[2][1]] = 'O'  # 장애물 세우기3

        if not bfs(y[0], y[1]):
            possible = 0

        graph_test = copy.deepcopy(graph_ori)

    if not possible:
        answer = 'NO'
    else:
        answer = 'YES'
        break

# 결과 출력
print(answer)
