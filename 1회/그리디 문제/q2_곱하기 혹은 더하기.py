# 나의 풀이
s = input()
result = int(s[0])
for i in range(1, len(s)):
  if result == 0 or result == 1:
    result += int(s[i])
  else:
    result *= int(s[i])
print(result)

# 답지 풀이
s = input()
result = int(s[0])
for i in range(1, len(s)):
  num = int(s[i])
  if result <= 1 or num <= 1:
    result += num
  else:
    result *= num
print(result)
