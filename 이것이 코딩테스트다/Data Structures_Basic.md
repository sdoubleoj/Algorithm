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

## 자료구조 Data Structure
- 데이터를 표현하고 관리하고 처리하기 위한 구조

<기초 개념>
- 스택 Stack
- 큐 Queue
- 재귀 함수 Recursive Function
    
<핵심 함수>
- 삽입 Push : 데이터 삽입
- 삭제 Pop : 데이터 삭제

    <고려사항>
    - 오버플로 Overflow
          특정한 자료구조가 수용할 수 있는 데이터의 크기를 이미 가득 찬 상태에서 삽입 연산 수행시, 즉 저장 공간을 벗어나 데이터가 넘쳐흐를 때 발생
    - 언더플로 Underflow
           특정한 자료구조에 데이터가 전혀 들어 있지 않은 상태에서 삭제 연산을 수행할 때 발생


 <br>
 
 ### 스택 Stack
 - "박스 쌓기"
 > **선입후출** Fisrt In Last Out(FILO) / **후입선출** Last In First Out(LIFO)
 - 시각화 : 입구와 출구가 동일한 형태
 - Python에서 스택 이용시 별도의 라이브러리 사용 필요 X,  기본 리스트에서 append()와 pop() 메서드 이용

```python
# 예제
stack = []

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1])
# arr[A:B:C] - index A 부터 index B 까지 C의 간격으로 배열을 만들어라
    # A가 None 이라면 처음부터
    # B가 None 이라면 할 수 있는 데까지 (C가 양수라면 마지막 index까지, C가 음수라면 첫 index까지)
    # 마지막으로 C가 None 이라면 한 칸 간격으로

```

### 큐 Queue
- "대기 줄"
> **선입선출** First In First Out(FIFO)
- 시각화 : 입구와 출구가 모두 뚫려있는 터널


#### **deque** 자료구조
    - collections 모듈에서 제공
    - Stack과 Queue의 장점 모두 채택
    - 데이터를 넣고 빼는 속도가 list 자료형에 비해 효율적 & queue 라이브러리를 이용하는 것보다 간단
        - list() 메서드로 자료형 변경 가능

```python
#예제
from collections import deque

queue = deque()

# 삽입(5) - 삽입(2) - 삽입(3) - 삽입(7) - 삭제() - 삽입(1) - 삽입(4) - 삭제()
queue.append(5) # 5
queue.append(2) # 2-5
queue.append(3) # 3-2-5
queue.append(7) # 7-3-2-5
queue.popleft() # 7-3-2
queue.append(1) # 1-7-3-2
queue.append(4) # 4-1-7-3-2
queue.popleft() # 4-1-7-3

print(queue) # 먼저 들어온 순서대로 출력
queue.reverse() # 다음 출력을 위해 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력
```

<br>

### 재귀 함수 Recursive Function
- 자기 자신을 재호출하는 함수...like 프랙털Fractal 구조

```python
def recursive_function():
    print('재귀 함수를 호출합니다.')
    recursive_function()

recursive_function()
```

- **recursive_function()** 이 자기 자신을 계속해서 추가로 불러오기 때문에, '재귀 함수를 호출합니다.'를 무한히 출력함
- Python Interpreter의 호출 횟수 제한 한계를 벗어나면 **RecursionError** 발생


<br>

#### 종료 조건
- 문제 풀이에서 사용시 재귀 함수가 언제 끝날지 종료 조건 명시 필수

```python
def recursive_function():
    
    # 100번째 출력했을 때 종료되도록 종료 조건 명시
    if i == 100:
        return
    
    print(i, '번째 재귀 함수에서', i+1, '번째 재귀 함수를 호출합니다')
    recursive_function(i+1)
    print(i, '번쨰 재귀 함수를 종료합니다')

recursive_function(1)
```

> 컴퓨터 내부적으로 Recursive Function은 Stack 자료구조와 동일
   - 함수를 계속 호출했을 때 가장 마지막에 호출한 함수가 먼저 수행을 끝내야 그 앞의 함수 호출이 종료되기 때문
       (+ 연속해서 호출되는 함수는 메인 메모리의 스택 공간에 적재되기 때문)
   - Stack 자료구조를 활용해야 하는 상당수 알고리즘은 Recursive Function을 이용해 간편하게 구현가능 (ex. DFS)


#### 대표 예제 : **팩토리얼 Factorial**
- 0!과 1!의 값이 1로 같다는 성질 이용, n이 1이하가 되었을 때 함수를 종료하는 형태


i) 반복적 구현

```python
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result
```

ii) 재귀적 구현

```python
def factorial_recursive(n):
    if n <= 1: #n이 1 이하인 경우 1을 반환
            return 1
    
    # n! = n * (n-1)!
    return n * factorial_recursive(n-1)
```

```python
print( factorial_iterative(5) )
print( factorial_recursive(5) )
```

> 재귀 함수 사용시 코드 간결

<**점화식(재귀식)** 사용한 코드 (중요)>

- 특정한 함수를 자신보다 더 작은 변수에 대한 함수와의 관계로 표현
    1. n == 0 or n == 1 : factorial(n) = 1
    2.            n > 1 : factorial(n) = n*factorial(n-1)
    
    <br>
    
- 고려사항
    - factorial은 n이 양의 정수일 때만 유효
    - n < 1인 경우를 고려하지 않으면 재귀함수 무한반복
