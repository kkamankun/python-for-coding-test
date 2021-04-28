n = int(input())
t_arr, p_arr = [0], [0]
d = [0] * (n + 1)
for _ in range(n):
    t, p = map(int, input().split())
    t_arr.append(t)
    p_arr.append(p)
for i in range(n, 0, -1):
    consulting_end_date = i + t_arr[i]
    if consulting_end_date > n + 1:
        d[i] = 0
        continue
    elif consulting_end_date == n + 1:
        d[i] = p_arr[i]
    else:
        d[i] = p_arr[i] + max(d[i + t_arr[i]:])
print(max(d))
