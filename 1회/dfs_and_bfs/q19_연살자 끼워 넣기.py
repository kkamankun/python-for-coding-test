# 나의 풀이
from itertools import permutations

n = int(input())
operand = list(map(int, input().split()))
operator = list(map(int, input().split()))
p = []
for i in range(4):
    for j in range(operator[i]):
        p.append(str(i))
p = set(map(''.join, permutations(p, len(p))))  # 같은 것이 있는 순열
candidate = []
for x in p:
    result = operand[0]
    for y in range(n - 1):
        if x[y] == '0':
            result += operand[y + 1]
        elif x[y] == '1':
            result -= operand[y + 1]
        elif x[y] == '2':
            result *= operand[y + 1]
        else:
            if result < 0:
                result = abs(result)
                result //= operand[y + 1]
                result = -result
            else:
                result //= operand[y + 1]

    candidate.append(result)
print(max(candidate))
print(min(candidate))
