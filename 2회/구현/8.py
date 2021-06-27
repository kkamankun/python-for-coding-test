S = input()

alpha = []
digit = 0
for s in S:
    if s.isalpha():
        alpha.append(s)
    else:
        digit += int(s)
alpha.sort()
answer = ''.join(alpha) + str(digit)
print(answer)
