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

# # Sequential Search
# ---
#   
# | (보통 정렬되지 않은) 리스트 내 특정 데이터를 찾기 위해 데이터를 '앞에서부터 하나끽 차례대로' 확인하는 방법
#
# - 가장 기본 탐색 알고리즘
# - 시간만 충분하다면 데이터가 아무리 많아도 항상 원하는 데이터를 찾을 수 있음
# - 특정 값의 원소가 있는지, count() 수행 내부, ..
#
# <br>
#

# +
def sequential_search(n, target, array):
    for i in range(n): #array의 첫번째 원소부터 시작하여
        if array[i] == target: #찾고자 하는 원소와 비교하여 같으면
            return i+1 #찾고자 하는 원소가 array의 i+1번째 원소와 같음을 출력
        
print("생성할 원소의 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.")
input_data = input().split()
n = int(input_data[0]) #원소의 개수
target = input_data[1] #찾고자 하는 문자열

print("앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.")
array = input().split()

#순자탐색 수행 결과 출력
print(sequential_search(n, target, array))


# -

#
# <br><br>
#
# # Binary Search
# ---
#   
#   
# | 탐색 범위를 반으로 좁혀가며 빠르게 탐색하는 알고리즘
#
# - 배열이 정렬되어 있어야만 사용 가능
# - 위치 변수 
#     - 시작점, 끝점, 중간점
#         - 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해 원하는 데이터를 찾음  
#         (중간점이 실수일 때는 소수점 이하 버림)
#
# <br>
#
# ## 시간 복잡도
# - $O(logN)$
#     - 확인할 때마다 확인하는 원소의 개수가 절반씩 줄어들기 때문 (퀵 정렬과 유사특징)
#     - 단계마다 2로 나누는 것과 동일하므로, 연산횟수는 $log_2 N$에 비례
#     
# <br>
#

# ## 구현
#   
# ### 재귀 함수 활용

# +
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start+end)//2
    
    #찾은 경우 중간점 인덱스 반환
    if array[mid] == target:
        return mid
    
    # 중간점의 값보다 찾고자 하는 값이 작은 경우 분할된 왼쪽 확인
    elif array[mid] > target:
        return binary_search(array, target, start, mid-1) #끝점 = 중간점-1
    
    #중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return binary_search(array, target, mid+1, end) #시작점 = 중간점+1
    
#n(원소 개수)와 target(찾고자 하는 문자열) 입력받기
n, target =  list(input().split())

# -

#
# <br>
#
# ### 반복문




