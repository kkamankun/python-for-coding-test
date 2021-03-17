n = int(input())
input_data = list(map(int, input().split()))
input_data.sort()
cnt = 0
result = 0
for i in input_data:
  cnt += 1
  if cnt >= i:
    result += 1
    cnt = 0
print(result)
