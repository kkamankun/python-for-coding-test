n = int(input())
coin = list(map(int, input().split()))

answer = 1
coin.sort()
for i in coin:
    if answer < i:
        break
    answer += i

print(answer)
