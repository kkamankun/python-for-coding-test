# 나의 코드
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

# 책 풀이
n, m = map(int, input().split())
input_data = list(map(int, input().split()))
# 볼링공의 무게별 개수를 저장할 배열 선언
arr = [0] * 11
for i in input_data:
    arr[i] += 1
result = 0
# 첫 번째 사람이 볼링공을 고르면, 두 번째 사람이 다른 무게의 볼링공을 고르는 조합의 수를 계산
for i in range(1, m+1):  # 공의 무게가 1부터 m까지
    n -= arr[i]
    result += arr[i] * n
print(result)
