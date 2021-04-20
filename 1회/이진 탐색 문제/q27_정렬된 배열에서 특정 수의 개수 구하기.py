# 나의 풀이
from bisect import bisect_left, bisect_right
import sys


# 값이 [left_value, right_value]인 데이터를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


n, x = map(int, sys.stdin.readline().rstrip().split())
array = list(map(int, sys.stdin.readline().rstrip().split()))

# 이진 탐색 수행 결과 출력
result = count_by_range(array, x, x)
if result == 0:
    print(-1)
else:
    print(result)
