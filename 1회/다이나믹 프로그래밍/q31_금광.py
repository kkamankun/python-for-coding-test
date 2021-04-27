def reshape(arr):
    _array = []
    row = []
    for i in range(n * m):
        if i % m == 0 and i > 0:
            _array.append(row)
            row = []
        row.append(arr[i])
    _array.append(row)
    return _array


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    array = reshape(list(map(int, input().split())))
    dp = [[0] * m for _ in range(n)]
    for i in range(n):
        dp[i][0] = array[i][0]
    for j in range(m - 1):
        for i in range(n):
            if i - 1 >= 0 and i + 1 < n:
                dp[i][j + 1] = max(dp[i - 1][j], dp[i][j], dp[i + 1][j]) + array[i][j + 1]
            elif i - 1 >= 0 and i + 1 >= n:
                dp[i][j + 1] = max(dp[i - 1][j], dp[i][j]) + array[i][j + 1]
            else:
                dp[i][j + 1] = max(dp[i][j], dp[i + 1][j]) + array[i][j + 1]

    answer = 0
    for i in range(n):
        answer = max(answer, dp[i][m - 1])
    print(answer)
