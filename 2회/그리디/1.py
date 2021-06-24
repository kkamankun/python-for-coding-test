n = int(input())
array = list(map(int, input().split()))

array.sort(reverse=True)
answer = 0
cnt = 0
x = array[0]
for i in range(len(array)):
    cnt += 1
    if x == cnt:
        answer += 1
        cnt = 0
        if i + 1 < len(array):
            x = array[i + 1]

print(answer)
