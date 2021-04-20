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

    
# 책의 풀이
n = int(input())
students = []  # 학생 정보를 담을 리스트

# 모든 학생 정보를 입력받기
for _ in range(n):
    students.append(input().split())

'''
[정렬 기준]
1) 두 번째 원소를 기준으로 내림차순 정렬
2) 두 번째 원소가 같은 경우, 세 번째 원소를 기준으로 오름차순 정렬
3) 세 번째 원소가 같은 경우, 네 번째 원소를 기준으로 내림차순 정렬
3) 네 번째 원소가 같은 경우, 첫 번째 원소를 기준으로 오름차순 정렬
'''
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# 정렬된 학생 정보에서 이름만 출력
for student in students:
    print(student[0])
