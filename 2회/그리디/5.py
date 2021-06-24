n, m = map(int, input().split())
ball = list(map(int, input().split()))

answer = 0
for i in range(n):
    w = ball[i]
    for j in range(i + 1, n):
        if w != ball[j]:
            answer += 1

print(answer)
