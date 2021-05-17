"""
서로소 집합 자료구조
도착한 비행기는 번호가 가장 높은 탑승구부터 도킹한다.
도킹 - union
도킹할 탑승구 찾기 - find
도킹할 탑승구와 번호가 하나 낮은 탑승구를 합집합 연산하여 루트 노드를 번호가 낮은 탑승구로 설정한다.
이를 통해, 최대로 도킹할 수 있는 비행기의 수를 효율적으로 구한다.
"""
G = int(input())  # G: 탑승구의 수
P = int(input())  # P: 비행기의 수

parent = [i for i in range(G + 1)]


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


answer = 0
for p in range(P):
    node = find_parent(parent, int(input()))
    if node == 0:
        break
    else:
        union_parent(parent, node, node - 1)
        answer += 1

print(answer)
