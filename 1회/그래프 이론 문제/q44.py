"""
효율성과 크루스칼 알고리즘을 함께 고려해야 하는 문제
모든 노드 사이의 거리를 완전 탐색으로 구현하면 효율성 문제 발생
따라서, 정렬을 활용하여 각 노드 사이의 비용을 계산하여 크루스칼 알고리즘 수행
시간 복잡도: O(ElogE)
"""
import sys
input = sys.stdin.readline


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
answer = 0
parent = [i for i in range(n)]

planet = []
for i in range(n):
    a, b, c = map(int, input().split())
    planet.append([a, b, c, i])

edges = []
# x좌표 기준으로 정렬
planet.sort(key=lambda x: x[0])
for i in range(n - 1):
    cost = abs(planet[i][0] - planet[i + 1][0])
    edges.append((cost, planet[i][3], planet[i + 1][3]))
# y좌표 기준으로 정렬
planet.sort(key=lambda x: x[1])
for i in range(n - 1):
    cost = abs(planet[i][1] - planet[i + 1][1])
    edges.append((cost, planet[i][3], planet[i + 1][3]))
# z좌표 기준으로 정렬
planet.sort(key=lambda x: x[2])
for i in range(n - 1):
    cost = abs(planet[i][2] - planet[i + 1][2])
    edges.append((cost, planet[i][3], planet[i + 1][3]))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        answer += cost

print(answer)
