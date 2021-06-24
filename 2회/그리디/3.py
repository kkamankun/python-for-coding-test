s = list(input())

x = s[0]
answer = 0
cnt = 0
for i in range(1, len(s)):
    if x != s[i]:
        x = s[i]
        cnt += 1
        if cnt == 2:
            answer += 1
            cnt = 0

if cnt == 1:
    answer += 1

print(answer)
