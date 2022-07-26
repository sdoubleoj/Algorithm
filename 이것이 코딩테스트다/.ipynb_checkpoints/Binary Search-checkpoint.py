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
# - 전제 : 데이터 정렬
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
#전체 원소 입력받기
array = list(map(int, input().split()))

#이진탐색 수행결과
result = binary_search(array, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result+1) 


# -

# - 나눈 몫만 얻기 : 몫 연산자(//) or int()

#
# <br>
#
# ### 반복문

# +
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start+end)//2
        
        #찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            return mid
        #중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target: #array[0] ~ array[mid-1]
            end =  mid-1
        #중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인 array[mid+1] ~ array[n-1]   
        else:
            start = mid+1
    
    return None

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result+1)
# -

# <br><br>
#
# ## @ 코테
# ---
#   
# - 구현 코드 암기 필수
#     - 코테 단골 문제
# - 다른 알고리즘에 적용되는 원리와 유사
# - 고난이도 문제에서는 이진탐색+다른 알고리즘 사용
# - 탐색 범위가 큰 상황에서의 탐색 문제 다수
#     - 탐색 범위 >= 2,000만 : 이진 탐색 접근
#     - 데이터 개수/값 >= 1,000만 단위 : 시간복잡도 $O(logN)$ 알고리즘 like 이진탐색

# <br><br>
#
# # Tree 자료구조
# ---
#  
# - 노드 간 연결로 표현
#     - 노드 : 정보의 단위, 어떠한 정보를 가지고 있는 개체  
#         ( == 그래프's 노드 (최단경로에서는 '정점' 의미) )  
#           
# - 그래프 자료구조의 일종
#     - DBS나 파일 시스템에서 대용량 데이터 관리 목적으로 사용
#
# - 특징
#     1. 부모 노드 - 자식 노드 관계로 표현
#     2. 최상단 노드 == 루트 노드
#     3. 최하단 노드 == 단말 노드
#     4. 트리 일부를 떼어내도 트리구조 == 서브 트리
#     5. 계층적, 정렬된 데이터 다루기 적합
#
# - 대용량 데이터 빠른 탐색 가능
# - 동작하는 프로그램에서는 데이터를 정렬해두는 경우가 많으므로, 이진탐색 효과적 사용
# - DB 활용성: 내부적으로 대용량 데이터 처리에 적합한 트리 자료구조를 이용해 항상 데이터가 정렬되어 있음 
#     => 이진탐색과 같은 알고리즘을 통한 탐색 효과적 활용
#       
# | 대용량 데이터를 처리하는 SW는 대부분 데이터를 트리 자료구조로 저장해 이진탐색과 같은 탐색 기법을 이용해 빠르게 탐색 가능
#
# <br>
#
# ## Binary Search Tree, BST
# --- 
#   
# - Tree 중 가장 간단한 형태
# - 이진 탐색이 동작할 수 있도록 고안된, 효율적인 탐색이 가능한 자료구조  
#   
#   
# - 성립조건 : 왼쪽 자식 노드 < 부모노드 < 오른쪽 자식 노드
#   
#   
# - 동작원리
#     - 루트노드부터 왼쪽 or 오른쪽 자식노드로 이동하며 반복 방문
#     - 자식노드가 없을 때까지 원소 탐색
#     

#       
# <br>
#
# ## readline()
# ---
#   
# - sys 라이브러리 함수
# - 입력 데이터가 많을 때 사용 ( N > 1,000만개 or 탐색범위 크기 > 1,000억)
#     - input()은 동작속도가 느려 시간초과될 수 있음
#     
# - 한 줄 입력받고 나서 rstrip() 호출 필수  
#     : realine()으로 입력 후 엔터가 줄바꿈 기호로 기호로 입력되어 생기는 공백문자 제거

# +
import sys

#하나의 문자열 데이터 입력
input_data = sys.stdin.readline().rstrip()

#입력받은 문자열 그대로 출력
print(input_data)
