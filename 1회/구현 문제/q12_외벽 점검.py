# 나의 
def solution(n, weak, dist):
    # 점검표 초기화
    checkList = [1] * n  # 1: 점검 완료, 0: 점검 필요
    for x in weak:
        if x == n:
            checkList[0] = 0
        else:
            checkList[x] = 0

    dist.sort(reverse=True)  # 점검 능력이 뛰어난 점검자부터 점검 내보내기
    checkInfo = dict()

    # 점검자 순차적으로 내보내기
    cnt = 0
    for x in dist:  # 점검 능력이 뛰어난 점검자부터 점검 내보내기
        cnt += 1
        max_checkCnt = 0
        for y in weak:  # 최적의 점검을 할 수 있도록 모든 점검 시작 지점 따져보기
            # 왼쪽으로 점검할 때 점검 예정인 지점 개수
            print(y-x, y+1)
            if y - x < 0:
                checkL = checkList[0:y+1].count(0)
            else:
                checkL = checkList[y-x:y+1].count(0)
            # 오른쪽으로 점검할 때 점검 예정인 지점 개수
            if y + x >= n:
                checkR = checkList[y:n].count(0)
                checkR += checkList[0:y+x-n+1].count(0)
            else:
                checkR = checkList[y:y+x+1].count(0)
            # 두 경우 중에 더 많이 점검할 수 있는 경우로 점검 예정
            if checkR > checkL:
                direction = 'R'
                checkCnt = checkR
            else:
                direction = 'L'
                checkCnt = checkL
            print('시작지점, 왼쪽, 오른쪽: ', y, checkL, checkR)
            if max_checkCnt < checkCnt:  # 가장 많이 점검할 수 있는 시작점과 방향 저장
                max_checkCnt = checkCnt
                checkInfo[x] = (y, direction)
        print('checkList: ', checkList)

        # 얻은 출발점과 점검 방향 정보를 바탕으로 점검 시작
        start, checkDir = checkInfo[x][0], checkInfo[x][1]
        print('start, dir: ', start, checkDir)
        if checkDir == 'R':
            if start + x < n:
                for i in range(start, start + x + 1):
                    checkList[i] = 1
            else:
                for i in range(start, n):
                    checkList[i] = 1
                for i in range(0, start + x - n + 1):
                    checkList[i] = 1
        else:  # checkDir == 'L'
            for i in range(start - x, start + 1):
                checkList[i] = 1

        # 점검표 점검
        if checkList.count(1) == n:  # 외벽 점검을 모두 완료했다면,
            answer = cnt  # 점검자 수를 반환
            return answer
    # 모든 점검자로 점검이 되지 않는 경우
    return -1


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
# print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
