# 나의 풀이
n = int(input())
array = []
for _ in range(n):
    temp = list(input().split())
    dic = dict()
    dic['이름'] = temp[0]
    dic['국어'] = int(temp[1])
    dic['영어'] = int(temp[2])
    dic['수학'] = int(temp[3])
    array.append(dic)
array.sort(key=lambda x: (-x['국어'], x['영어'], -x['수학'], x['이름']))
for data in array:
    print(data['이름'])
