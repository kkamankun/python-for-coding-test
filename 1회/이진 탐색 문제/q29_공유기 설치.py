import sys

# 집의 개수(N)와 공유기의 개수(C)를 입력받기
n, c = map(int, sys.stdin.readline().rstrip().split())
# 각 집의 좌표 정보를 입력받기
array = []  # 집의 좌표의 값은 최대 10억까지의 정수
for _ in range(n):
    array.append(int(sys.stdin.readline()))
array.sort()

# 이진 탐색을 위한 시작점과 끝점 설정
end = array[-1] - array[0]
start = 1

# 이진 탐색 수행(반복적)
result = 0
while start <= end:
    value = array[0]
    count = 1
    mid = (start + end) // 2  # gap을 조정하며 공유기를 설치해보기
    for i in range(1, n):
        if array[i] >= value + mid:
            value = array[i]
            count += 1
    if count >= c:  # 공유기를 c개보다 더 설치할 수 있으면 gap을 늘려보기
        result = mid
        start = mid + 1
    else:  # 공유기를 c개보다 덜 설치할 수 있으면 gap을 줄여보기
        end = mid - 1
print(result)
