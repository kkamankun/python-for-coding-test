n = int(input())
array = []
for _ in range(n):
    array.append(list(map(int, input().split())))
dp = [[0] * n for _ in range(n)]
dp[0][0] = array[0][0]
for i in range(1, n):
    for j in range(n):
        if i < j:
            continue
        if j - 1 >= 0 and j < i:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i - 1][j]) + array[i][j]
        elif j - 1 >= 0 and j == i:
            dp[i][j] = dp[i - 1][j - 1] + array[i][j]
        else:
            dp[i][j] = dp[i - 1][j] + array[i][j]
answer = max(dp[n - 1])
print(answer)
