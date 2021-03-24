s = input()
n = len(s)
t1, t2 = 0, 0
for i in range(n//2):
  t1 += int(s[i])
for j in range(n//2, n):
  t2 += int(s[j])
if t1 == t2:
  print('LUCKY')
else:
  print('READY')
  
