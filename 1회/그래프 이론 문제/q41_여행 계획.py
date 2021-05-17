"""
서로소 집합 알고리즘
여행지가 연결되어 이동이 가능한가?
: 같은 집합에 속해있으면 가능하다.
같은 집합에 속해있는가?
: 루트 노드가 같으면 같은 집합에 속해있다.
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # n: 여행지의 수, m: 여행 계획에 속한 도시의 수
connected = [list(map(int, input().split())) for _ in range(n)]
# 여행 계획에 포함된 여행지의 번호들
plan = list(map(int, input().split()))

# 서로 연결된 두 노드들
road = [(i + 1, j + 1) for i in range(n) for j in range(n) if connected[i][j] == 1]

parent = [i for i in range(n + 1)]


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


for r in road:
    a, b = r
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)


answer = "YES"
for i in range(m - 1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i + 1]):
        answer = "NO"
        break
print(answer)
