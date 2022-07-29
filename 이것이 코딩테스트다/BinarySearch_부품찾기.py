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
# 부품 N개 ( 1<= N <= 1,000,000)
# 각 부품 정수 고유번호 ( 1 이상, 1,000,000 이하)
# M개 부품 확인요청 ( 1 <= M <= 100,000)

#반복문 구현
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid-1
        else:
             start = mid+1
    return None

#가게 부품 개수
n = int(input())
#전체 부품 고유번호
array = list(map(int, input().split()))
array.sort()

#손님이 확인 요청한 부품 개수
m = int(input())
#확인요청한 부품 고유번호
x = list(map(int, input().split()))

#부품 하나씩 확인
for i in x:
    result = binary_search(array, i, 0, n-1)
    if result != None:
        print('yes', end = ' ')
    else:
        print('no', end=' ')

# +
#계수정렬 구현
n - int(input())
array = [0] * 1000001

#가게에 있는 부품 전체의 고유번호
for i in input().split():
    array[int(i)] = 1
    
m = int(input())
x = list(map(int, input().split()))

for i in x:
    if array[i] == 1:
        print('yes',end=' ')
    else:
        print('no',end=' ')

# +
#집합 자료형 이용
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end=' ')
    else:
        print('no', end=' ')
