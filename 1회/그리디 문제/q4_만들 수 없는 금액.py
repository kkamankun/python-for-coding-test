# 나의 코드
n = int(input())
input_data = list(map(int, input().split()))
input_data.sort()
cnt_list = [0] * 100
for i in range(0, n - 1):
  for j in range(i + 1, n):
    cnt_list[input_data[i] + input_data[j]] += 1
for i in range(0, n):
  if cnt_list[i] == 0:
    print(i + 1)
    break

# 책 코드
'''
현재 상태를 '1부터 target-1까지의 모든 금액을 만들 수 있는 상태'라고 보자.
이때 매번 target인 금액도 만들 수 있는지 체크하는 것이다.
'''
n = int(input())
input_data = list(map(int, input().split()))
input_data.sort()
target = 1
for i in input_data:
  if target >= i:
    target += i
print(target)
