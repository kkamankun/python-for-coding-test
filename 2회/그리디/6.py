import heapq


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    food = []
    for i in range(len(food_times)):
        heapq.heappush(food, (food_times[i], i + 1))
    now = food[0][0]
    previous = 0
    n = len(food_times)

    while k > (now - previous) * n:
        now = heapq.heappop(food)[0]
        k -= (now - previous) * n
        n -= 1
        previous = now
        now = food[0][0]

    food.sort(key=lambda x: x[1])
    answer = food[k % n][1]

    return answer


# print(solution([3, 1, 2], 5))
print(solution([8, 4, 9], 15))
