# 내 풀이
import itertools

n, m = map(int, input().split())
input_data = list(map(int, input().split()))
temp = []
for i in input_data:
  if i <= m:
    temp.append(i)
result = list(itertools.combinations(temp, 2))
for x in result:
  if x[0] == x[1]:
    result.remove(x)
print(len(result))
