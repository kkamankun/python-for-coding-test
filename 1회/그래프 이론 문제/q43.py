"""
크루스칼 알고리즘
최소 신장 트리를 구하여 비활성화할 간선을 선택하여 값을 모두 더하면 된다.
"""
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


N, M = map(int, input().split())  # N: 노드의 개수, M: 간선의 개수
edges = []
answer = 0
parent = [i for i in range(N + 1)]
for _ in range(M):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
    else:
        answer += cost
        print(cost, a, b)

print(answer)
