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
    - 선택정렬과 삽입정렬이 최악에도 $O(N^2)$를 보장하므로 퀵정렬은 매우 빠름

```python

```

<!-- #region -->
<br><br>


# 계수 정렬 Count Sort
<!-- #endregion -->

```python

```

```python

```
