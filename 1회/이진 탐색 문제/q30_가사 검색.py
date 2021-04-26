# 나의 풀이
from bisect import bisect_left, bisect_right


def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index


def solution(words, queries):
    word_len = dict()
    for w in words:
        try:
            word_len[len(w)].append(w)
        except KeyError:
            word_len[len(w)] = [w]
    for k in word_len.keys():
        word_len[k].sort()
    _word_len = dict()
    for k in word_len.keys():
        for x in word_len[k]:
            try:
                _word_len[-k].append(x[::-1])
            except KeyError:
                _word_len[-k] = [x[::-1]]
    for k in _word_len.keys():
        _word_len[k].sort()
    answer = []
    for q in queries:
        n = len(q)
        left_value = q.replace('?', 'a')
        right_value = q.replace('?', 'z')
        if q[0] == '?':  # prefix
            try:
                answer.append(count_by_range(_word_len[-n], left_value[::-1], right_value[::-1]))
            except KeyError:
                answer.append(0)
        else:  # suffix
            try:
                answer.append(count_by_range(word_len[n], left_value, right_value))
            except KeyError:
                answer.append(0)

    return answer
