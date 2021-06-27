def solution(s):
    answer = len(s)
    for unit in range(1, len(s)):
        candidate = ''
        cnt = 1
        cur = 0
        while True:
            if cur + 2*unit > len(s):
                rest = s[cur:]
                if cnt > 1:
                    candidate += str(cnt)
                candidate += rest
                break
            word = s[cur:cur+unit]
            next_word = s[cur+unit:cur+2*unit]
            if word == next_word:
                cnt += 1
            else:
                if cnt > 1:
                    candidate += str(cnt)
                candidate += word
                cnt = 1
            cur += unit
        answer = min(answer, len(candidate))

    return answer


# print(solution('aabbaccc'))
