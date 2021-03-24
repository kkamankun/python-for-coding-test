def solution(s):
  cnt = 1
  min = len(s)
  for unit in range(1, len(s)):  # 한 단계씩 증가시키며 확인
    result = ''
    for i in range(0, len(s), unit):
      if s[i:i+unit] != s[i+unit:i+(2*unit)]:
        if cnt > 1:
          result += str(cnt)
        result += s[i:i+unit]
        cnt = 1
      else:
        cnt += 1
    if len(result) < min:
      min = len(result)
  return min
