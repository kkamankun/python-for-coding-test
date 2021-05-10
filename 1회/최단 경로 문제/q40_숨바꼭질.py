import heapq
INF = int(1e9)

n, m = map(int, input().split())  # n: 헛간(노드)의 개수, m: 통로(간선)의 개수
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    # 양방향 통로
    graph[a].append((b, 1))
    graph[b].append((a, 1))
distance = [INF] * (n + 1)
start = 1

q = []
heapq.heappush(q, (0, start))
distance[start] = 0
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        # 만약 다른 노드를 거쳐서 가는 것이 더 빠르다면 초기화
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

max_distance = 0
for d in distance:
    if d == INF:
        continue
    if max_distance < d:
        max_distance = d
print(distance.index(max_distance), max_distance, distance.count(max_distance))
