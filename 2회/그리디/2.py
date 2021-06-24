s = list(map(int, input()))

s.sort(reverse=True)
answer = s[0]
for i in range(1, len(s)):
    if s[i] == 0 or s[i] == 1:
        answer += s[i]
    else:
        answer *= s[i]

print(answer)
