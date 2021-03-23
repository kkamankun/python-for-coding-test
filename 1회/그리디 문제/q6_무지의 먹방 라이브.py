# 나의 코드
def solution(food_times, k):
    cur_food = 0
    for i in range(k):
        food_times[cur_food] -= 1
        cur_food += 1
        if cur_food == len(food_times):
            cur_food = 0
        else:
            while food_times[cur_food] == 0:
                cur_food += 1
                if cur_food == len(food_times):
                    cur_food = 0
                    break
    answer = cur_food
    return answer + 1

# 책의 풀이
import heapq  # 우선순위 큐(Min 힙)


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    q = []
    # 모든 음식을 시간을 기준을 정렬
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))  # (각 음식을 먹는 데 필요한 시간, 해당 음식의 번호)
    sum_value = 0  # 먹기 위해 사용한 시간
    previous = 0  # 이전 음식을 먹는 데 필요했던 시간
    length = len(food_times)  # 남아 있는 음식의 개수
    while sum_value + (q[0][0] - previous) * length <= k:
        now = heapq.heappop(q)[0]  # 현재 음식을 먹는 데 필요한 시간
        sum_value += (now - previous) * length
        length -= 1
        previous = now
    # 음식의 번호 순서로 남아있는 음식들을 정렬
    result = sorted(q, key=lambda x: x[1])
    return result[(k - sum_value) % length][1]


print(solution([3, 1, 2], 5))
