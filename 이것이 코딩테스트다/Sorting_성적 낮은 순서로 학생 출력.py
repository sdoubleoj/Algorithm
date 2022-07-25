# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
#학생 수
n = int(input())

students = []
#학생 (이름, 성적) 튜플 리스트
for _ in range(n):
    name, score = input().split()
    students.append((name, int(score)))

#정렬 기준인 성적 출력 함수
def setting(array):
    return array[1]

#성적 낮은 순으로 이름 출력
students = sorted(students, key=setting) #or.. sorted(students, key = lambda student : student[1])

for i in students:
    print(i[0], end=' ')
