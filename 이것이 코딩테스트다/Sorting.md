---
jupyter:
  jupytext:
    formats: ipynb,md
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.14.0
  kernelspec:
    display_name: Python 3 (ipykernel)
    language: python
    name: python3
---

# Sorting
--- 

- 데이터를 특정 기준에 따라 순서대로 나열
- 이진탐색Binary Search의 전처리 과정
- '알고리즘 효율성'에 방점

<br><br>



# 선택 정렬, Selection Sort
---

- '매번 가장 작은 것을 선택'
- 가장 작은 데이터를 앞으로 보내는 과정 N-1번 반복

<br>

## 소스코드

```python
array = [7,5,9,0,3,1,6,2,4,8]

#모든 원소를 비교하고 위치 교체
for i in range(len(array)): # 0 ~ N-1
    min_index = i #최솟값 인덱스
    for j in range(i+1,len(array)):
        if array[min_index] > array[j]:
            min_index = j #최솟값 인덱스 번호 갱신
        arrya[i], array[min_index] = array[min_inedx], array[i] #스와프

print(array)
```

<br>

### 스와프Swap
- 특정한 리스트가 주어졌을 때 두 변수의 위치 변경

```python
# 0 인덱스와 1 인덱스의 원소 교체
array = [3,5]
array[0], array[1] =array[1],array[0]

print(array)
```

<!-- #region -->
<br>

## 시간 복잡도
  
- $O(N^2) \qquad$   ..반복문 중첩 정도 기준
- 최악의 경우에도 $O(N^2)$ 보장
- (N-1)번 만큼 최솟값을 찾아 첫번째로 보내야 함 + 매 반복마다 최솟값을 찾기 위한 비교연산 필요  

    => N + (N-1) + (N-2) + .. + 2  
    => $N * (N-1)/2$번의 연산  
    => $(N^2 + N)/2$  
    => $O(N^2)$
    
<br>

## 효율
  
- 이론상 데이터의 수 N이 100배 증가하면, 수행시간은 10,000배 증가
- 다른 알고리즘과 비교했을 때, N이 10,000을 넘어가면 비효율 급속 증가


<br><br>

<!-- #endregion -->

# 삽입 정렬, Insertion Sort
---
  
> 데이터를 하나씩 확인하며, 각 데이터를 적절한 위치에 삽입

- 정렬되어 있는 데이터 리스트에서 적정위치를 찾아 그 위치에 특정 데이터를 삽입  
    - 가정: 특정 위치 앞까지의 데이터는 이미 정렬된 상태  
    => 2번쨰 데이터부터 정렬 시작
    
- 선택 정렬에 비해 실행시간 측면에서는 더 효율적
- 




<br>

## 소스코드

```python
array = [7,5,9,0,3,1,6,2,4,8]


for i in range(1,len(array)): #1 ~ N-1 : 첫번째 데이터는 그 자체로 정렬되어 있다고 간주
    for j in range(i,0,-1): #오름차순 정렬이므로 왼쪽 이동 (i,i-1,..,1)(데이터가 왼쪽으로(-1) 인덱스 이동하는거 따라가는 것)
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j] #스와프
        else: #자기보다 작은 데이터를 만나면 그 위치에서 탐색 멈춤
            break
            
print(array)
```

<br>

## 시간 복잡도
  
- worst: $O(N^2) \qquad$ ..반복문 2중첩
    - 선택 정렬과 유사
- best(데이터가 거의 정렬되어 있는 상태): $O(N)$ 
    - 퀵 정렬보다 효율적
    
<br><br>



# 퀵 정렬, Quick Sort
---
  
> 설정한 기준에 따라 큰 수와 작은 수를 교환한 후, 리스트를 반으로 분할

- 가장 많이 사용되는 알고리즘 (+ 벙합 정렬)  
<br>
- '기준' == 피벗
    - 피벗 설정 선행 필수
    
<br><br>



## 호어 분할 Hoare Partition
  
> 리스트의 첫 번쨰 데이터를 피벗으로 설정
- 가장 대표적 분할 방식  

1. 첫 번째 데이터를 피벗으로 설정
    1. 왼쪽에서부터 피벗보다 큰 데이터를, 오른쪽에서부터 피벗보다 작은 데이터를 찾음
    2. 큰 데이터와 작은 데이터 스와프
    3. 1~2 반복, 왼쪽과 오른쪽에서 찾는 값의 위치가 엇갈린 경우 작은 데이터와 피벗 스와프
    4. 피벗까지 이동하여 피벗의 왼쪽에는 모두 작은, 오른쪽에는 모두 큰 데이터가 위치하도록 분할/파티션 완료
2. A~D 방식으로 피벗의 왼쪽 & 오른쪽 리스트 개별 정렬

<br><br>



## 소스코드
- 재귀함수와 동작원리 같으므로, 재귀함수 형태로 구현시 간결

<br>

### ver 1

```python
array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array, start, end):
    if start >= end: #종료조건: 리스트 원소가 1개인 경우
        return
    
    #인덱스 지정
    pivot = start #피벗 설정: 가장 첫 번째 원소
    left = start + 1
    right = end
    
    #탐색 시작
    while left <= right:
        while left <= end and array[left] <= array[pivot]: #피벗보다 큰 데이터를 찾을 때까지 이동 반복
            left += 1
        while right > start and array[right] >= array[pivot]: #피벗보다 작은 데이터를 찾을 때까지 이동 반복
            right += 1
        
        #각각 큰/작은 데이터를 찾은 후,
        if left > right: #큰/작은 데이터의 위치가 엇갈린 경우, 작은데이터(right)와 피벗 swap
            array[right], array[pivot] = array[pivot], array[right]
        else: #엇갈리지 않았다면, 큰/작은 데이터 swap
            array[left], array[right] = array[right], array[left]
            
    #1차 분할 완료 후, 왼쪽/오른쪽 리스트 개별 정렬
    quick_sort(array, start, right-1) #원래 피벗의 현 위치 == right
    quick_sort(array, right+1, end)
    
quick_sort(array, 0, len(array)-1) # array[0] ~ array[N-1] == N
print(array) 
```

<br>

### ver 2 - 파이썬 장점 활용
  
- 피벗과 데이터 비교연산 횟수 증가로 시간적 비효율성, but 직관적 & 기억하기 쉬움

<br>


```python
array = [7,5,9,0,3,1,6,2,4,8]

def quick_sort(array):
    #종료조건: 리스트 원소가 1개인 경우
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    tail = array[1:] #피벗 제외 리스트
    
    #분할
    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]
    
    #분할 이후, 왼쪽과 오른쪽 리스트 개별 정렬 수행하여 전체 리스트 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))
```

<br><br>

## 시간 복잡도
  
- 평균 : $O(NlogN)$
    - 선택정렬과 삽입정렬이 최악에도 $O(N^2)$를 보장하므로 매우 빠른 것임
    - 단, 데이터가 '무작위'로 입력될 경우의 복잡도  
  
- 최악 : $O(N^2)$
    - 이미 데이터가 정렬되어 있는 경우
        - 삽입 정렬과는 반대의 성질  
  
- 기본 제공의 정렬 라이브러리가 피벗값 설정시 '추가적인 로직'을 더해주기 때문에 최악의 경우에도 $O(NlogN)$을 보장할 수 있도록 해줌

<!-- #region -->
<br><br>


# 계수 정렬 Count Sort
---
1. 효율성
    - 데이터의 크기가 한정되어 있을 경우, 데이터의 개수가 매우 많더라도 빠르게 동작  
        - 데이터의 크기 범위가 제한되어 정수 형태로 표현할 수 있을 때만 가능
        - 일반적으로, (데이터 최댓값 - 최솟값 <= 1e6)일 때 효과적
        
    - 데이터 크기가 많이 중복되어 있을수록 유리
    - 단, 데이터 최댓값과 최솟값의 차이가 너무 크면 사용 불가
        - 계수정렬 사용시 모든 범위를 담을 수 있는 크기의 리스트(배열)을 선언해야 하기 때문
    
2. 데이터의 개수 N & 데이터 중 최댓값 K 일 때, 최악의 경우에도 $O(N+K)$ 보장

3. 계수 정렬은 별도의 리스트를 선언하고, 그 안에 정렬에 대한 정보를 담음
    - 선택/삽입/퀵 정렬과 같은 '비교 기반'의 정렬 알고리즘이 아님

<br><br>

## 동작
1. 리스트 선언 : 인덱스가 데이터의 모든 범위를 포함할 수 있도록  
    ex. 데이터 범위: 0~9 -> 크기가 10인 리스트 선언  
    
2. 리스트 모든 원소 0 초기화

3. 데이터를 하나씩 학왼, 데이터 값과 동일한 인덱스의 데이터를 1씩 증가  
    - 각 데이터의 '등장횟수' 기록
    - 리스트에 저장된 자체가 정렬된 형태 그 자체
    
4. 정렬 결과 > 첫 번째 데이터부터 하나씩 그 값만큼 인덱스 출력
<!-- #endregion -->

<br><br>

## 소스코드

```python
# 모든 원소의 값이 0보다 크다고 가정
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2]

# 모든 범위를 포함하는 리스트 선언 (모든 값 0으로 초기화)
count = [0] * (max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1 # array의 각 데이터 (0~9) == count의 인덱스 번호, count 원소 == 각 데이터 등장 횟수
    
# 정렬 결과 출력
for i in range(len(count)): # 데이터 0~9
    for j in range(count[i]): # count[j] == 데이터 j의 등장횟수
        print(i, end=' ')
```

<br><br>

## 시간 복잡도

- $O(N+K)$
    - 앞에서부터 데이터를 하나씩 확인하면서 리스트에서 적절한 인덱스의 값을 1씩 증가 &  
        추후에 리스트의 각 인덱스에 해당하는 값들을 확인할 때 데이터 중 최댓값의 크기(K)만큼 반복 수행

- 정렬 알고리즘 중 가장 빠름 (+ 기수정렬)

<br><br>

## 공간 복잡도

- $O(N+K)$
- 비효율성
    - 데이터가 0과 99,999,999 단 2개만 존재할 경우, 100만 크기의 리스트를 선언해야 하기 떄문에 심각한 비효율성 발생
    - 데이터 특성 파악이 어렵다면 (평균적으로 빠르게 동작하는) 퀵 정렬이 유리
    
<br><br>



# 파이썬의  정렬 라이브러리
---  

- 직접 정렬 알고리즘 짜는 것보다 효과적인 경우 많음

<br><br>

## sorted()
  
- 병합 정렬 기반 (퀵 정렬과 동작방식 유사)
    - 병합 정렬 ?
        - 일반적으로 퀵 정렬 보다 느림
        - 최악의 경우에도 시간 복잡도 $O(NlogN)$ 보장  
        (퀵 정렬 기반 함수도 $O(NlogN)$ 보장하도록 구현되어 있음)
- List, Set, Dictionary 자료형 등 입력, 리스트 반환

<br>


```python
array = [7,5,9,0,3,1,6,2,4,8]

result = sorted(array)
print(result)
```

<br><br>

## sort()
- 리스트 변수가 한 개 있을 때, 바로 정렬
- 별도의 정렬된 리스트를 리턴하지 않음
    - 주의) 반환값이 없으므로 array = array.sort() 할 경우, array는 None type이 됨

<br>

```python
array = [7,5,9,0,3,1,6,2,4,8]
array.sort()
print(array)
```

<br><br>

## key 매개변수

- sort()나 sorted() 이용시 활용
- 함수 (사용자지정 or 람다)
- 정렬 기준


```python
array = [('banana',2), ('apple',5),('carrot',3)]

def setting(data):
    return data[1]

result = sorted(array, key=setting)
print(result)
```

<br><br>

## 시간 복잡도
- 최악의 경우에도 $O(NlogN)$ 보장
- 병합 정렬+삽입 정렬인 알고리즘이므로 퀵 정렬 직접 구현하는 것보다 더욱 효과적

<br><br>

<!-- #region -->
# 정렬 알고리즘이 사용되는 문제 유형
---
<br>

1. 정렬 라이브러리로 풀 수 있는 문제
    - 단순히 정렬 기법을 알고 있는지 물어보는 문제
    - 사용법 숙지하고 있으면 쉬움
      
      
2. 정렬 알고리즘 원리에 대해 물어보는 문제
    - 각 정렬 알고리즘의 원리 숙지 필수
      
      
3. 더 빠른 정렬 필요한 문제
    - 퀵 정렬 기반의 정렬 기법 사용불가
    - 계수 정렬 등의 다른 알고리즘 이용 or 문제에서 기존에 알려진 알고리즘의 구조적인 개선 필요
<!-- #endregion -->
