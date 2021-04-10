# 나의 풀이
def is_pair(s):
    stack = []
    for ch in s:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            try:
                stack.pop()
            except IndexError:
                return False
    return len(stack) == 0


def reverse(s):
    r_s = ''
    for ch in s:
        if ch == '(':
            r_s += ')'
        else:
            r_s += '('
    return r_s


def solution(p):
    if p == '':
        return ''
    u, v = '', ''
    for i in range(len(p)):
        u += p[i]
        if u.count('(') == u.count(')'):
            v = p[i + 1:]
            break
    if is_pair(u):
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + reverse(u[1:len(u) - 1])
