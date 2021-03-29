# 나의 풀이
from itertools import combinations


def manhattan_distance(pt1, pt2):  # 점1, 점2
    result = 0
    for i in range(len(pt1)):
        result += abs(pt2[i] - pt1[i])
    return result


n, m = map(int, input().split())  # 마을의 크기: n, 최대 치킨집의 개수: m
town = []
for _ in range(n):
    town.append(list(map(int, input().split())))
home_coordinate, chicken_coordinate = [], []  # 인덱스 1부터 시작하게 만들기 위함
for i in range(n):
    for j in range(n):
        if town[i][j] == 1:  # 가정집 좌표 저장
            home_coordinate.append([i, j])
        elif town[i][j] == 2:  # 초기 치킨집의 좌표 저장
            chicken_coordinate.append([i, j])
        else:
            pass
home_cnt = len(home_coordinate)
chicken_cnt = len(chicken_coordinate)
combinations_result = list(combinations(chicken_coordinate, m))

# M개의 치킨집을 뽑을 수 있는 모든 경우의 수를 따져보면서
min_chickenDistance = float("inf")
for i in combinations_result:
    chickenDistance = 0
    for j in range(home_cnt):  # 가정집을 하나씩 기준으로
        min_homeToChicken = float("inf")
        for k in range(m):  # 가장 가까운 곳에 위치한 치킨집으로의 치킨거리의 맨하탄 거리를 구하여
            dist = manhattan_distance(home_coordinate[j], i[k])
            min_homeToChicken = min(min_homeToChicken, dist)
        chickenDistance += min_homeToChicken  # 치킨거리의 합을 구하기
    min_chickenDistance = min(min_chickenDistance, chickenDistance)
    
# 결과 출력
answer = min_chickenDistance
print(answer)
