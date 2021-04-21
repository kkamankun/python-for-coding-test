# 나의 풀이
# 이진 탐색 소스코드 구현(재귀 함수)
def binary_search(array, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 찾은 경우 중간점 인덱스 반환
    if array[mid] == mid:
        return mid
    # 중간점의 값이 인덱스보다 작은 경우 왼쪽 확인
    elif array[mid] > mid:
        return binary_search(array, start, mid - 1)
    # 중간점의 값이 인덱스보다 큰 경우 오른쪽 확인
    else:
        return binary_search(array, mid + 1, end)


# n(원소의 개수)와 전체 원소 입력받기
n = int(input())
array = list(map(int, input().split()))

# 이진 탐색 수행 결과 출력
result = binary_search(array, 0, n - 1)
if result is None:
    print(-1)
else:
    print(result)
