import heapq

INF = int(1e9)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

t = int(input())
for _ in range(t):
    n = int(input())
    graph = []
    for _ in range(n):
        graph.append(list(map(int, input().split())))
    distance = [[INF] * n for _ in range(n)]

    q = []
    heapq.heappush(q, (graph[0][0], (0, 0)))
    distance[0][0] = graph[0][0]
    while q:
        dist, now = heapq.heappop(q)
        x, y = now
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if distance[x][y] + graph[nx][ny] < distance[nx][ny]:
                distance[nx][ny] = distance[x][y] + graph[nx][ny]
                heapq.heappush(q, (distance[nx][ny], (nx, ny)))
    print(distance[-1][-1])
