INF = int(1e9)

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

# 모든 지점에서 다른 모든 지점까지의 최단 경로 구하기
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

answer = 0
for a in range(1, n + 1):
    count = 0
    for b in range(1, n + 1):
        if graph[a][b] != INF or graph[b][a] != INF:
            count += 1
    if count == n:
        answer += 1
print(answer)
