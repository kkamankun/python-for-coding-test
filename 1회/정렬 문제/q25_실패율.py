def solution(N, stages):
    answer = []
    t = len(stages)
    for i in range(1, N + 1):
        cnt = stages.count(i)

        if t == 0:
            fail = 0
        else:
            fail = cnt / t  # 실패율 계산
        answer.append((i, fail))
        t -= cnt

    answer.sort(key=lambda x: x[1], reverse=True)
    return [i[0] for i in answer]
