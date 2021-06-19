T = int(input())  # 테스트케이스 개수
for t in range(T):
    N = int(input())  # 팀의 수
    last_year_order = list(map(int, input().split()))
    M = int(input())
    teams_order_changed = [tuple(map(int, input().split())) for _ in range(M)]

    answer = []





    if len(answer) == 0:
        print("IMPOSSIBLE")
    else:
        for n in range(N):
            print(answer[n], end=" ")
