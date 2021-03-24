from collections import deque

s = list(input())
s.sort()
q = deque(s)
t = 0
while 48 <= ord(q[0]) <= 57:
  t += int(q[0])
  q.popleft()
answer = ''
for x in list(q):
  answer += x
print(answer + str(t))
