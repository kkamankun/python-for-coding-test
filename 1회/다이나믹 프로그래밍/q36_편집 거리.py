str1 = input()
str2 = input()
n, m = len(str1), len(str2)
d = [[0] * m for _ in range(n)]
for i in range(n):
    d[i][0] = i
for j in range(m):
    d[0][j] = j

for i in range(1, n):
    for j in range(1, m):
        if str1[i] == str2[j]:
            d[i][j] = d[i - 1][j - 1]
        else:
            d[i][j] = min(d[i - 1][j], d[i - 1][j - 1], d[i][j - 1]) + 1
print(d[-1][-1])
