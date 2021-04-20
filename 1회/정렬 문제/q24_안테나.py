""" 나의 풀이 """
import sys

n = int(sys.stdin.readline().rstrip())
input_data = list(map(int, sys.stdin.readline().rstrip().split()))
input_data.sort()
cnt = 0
for i in input_data:
    cnt += 1
    if cnt >= n // 2:
        break
print(i)

""" 책의 풀이 """
n = int(input())
data = list(map(int, input().split()))
data.sort()

# 중간값(median)을 출력
print(data[(n - 1) // 2])
