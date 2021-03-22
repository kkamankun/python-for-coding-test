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
