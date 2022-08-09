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

# Dinamic Programming
    한 번 계산한 문제는 다시 계산하지 않도록 하는 알고리즘

- 동적 계획법
- 메모리 공간을 더 사용하여 연산 속도를 비약적으로 증가시킴
- 자료구조의 '동적 할당(Dinamic Allocation)'과 다름
    - 동적 할당 : *프로그램 실행* 중에 이에 필요한 메모리를 할당하는 기법
- 사용조건
    1. 큰 문제를 작은 문제로 나눌 수 있음
    2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일
- 조건1은 퀵 정렬에서 리스트를 분할하여 리스트 전체를 정렬하는 것과 동일함 == '분할 정복Divide and Conquer 알고리즘'  
  단, DP는 작은 문제들이 서호 영향을 미치고 있다는 점에서 차이.
  
<br><br>
  
## 대표문제: 피보나치 수열
    이전 두 항의 합을 현재의 항으로 설정
    
- 점화식 (인접한 항 간의 관계식)  
  : $a_{n+1} = f( a_{n-1} ,a_n ) = a_{n+1} + a_n$
  ; 인접 3항간 점화식

<br>

## Top-Down DP
    재귀함수를 이용한 DP 소스코드 작성
    ; 큰 문제를 해결하기 위해 작은 문제 호출
<br>

### 소스코드

```python
#피보나치 함수를 재귀함수로 구현(탑다운)
def fibo(x):
    if x==1 or x==2:
        return 1
    
    return fibo(x-1) + fibo(x-2)

print(fibo(4))
```

<br><br>

## Memoization (== Chaching)
    한 번 구한 결과를 메모리 공간에 메모해두고(리스트에 값 저장) 같은 식을 다시 호출하면 메모한 결과를 그대로 가져오는 기법

- 탑다운 방식에만 사용되는 표현
- 한 번 구한 정보는 리스트에 저장.  
  재귀적으로 수행하다가 중복되는 정보가 필요할 때는 이미 구한 정답을 그대로 리스트에서 가져옴
    
<br>

### 소스코드 (재귀적) : 탑다운 메모제이션 방식

```python
#한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0] * 100

#Fibonacci Func를 재귀함수로 구현 (탑다운 DP)
def fibo(x):
    
    #종료 조건 (1 or 2일 때 1 반환)
    if x==1 or x==2:
        return 1
    
    #이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    
    #아직 계산하지 않은 문제라면 점화식에 따라 피보나치 결과 반환
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))
```

* 사실상 호출되지는 않는 노드라고 하더라도, 재귀함수를 사용하면 메모리 상에 적재되는 과정이 필수적이므로 '오버헤드' 발생 가능  
    => 반복문을 이용한 DP 이용 (오버헤드 ↓ 성능↑)
    
<br>

## setrecursionlimit( )
    sys 라이브러리의 재귀 제한 완화 함수 
    
<br>

## 시간 복잡도
- $O(N)$
- 한 번 구한 $f(a_{n-1})$이 $f(a_n)$을 구하는데 사용되기 때문

```python
#함수가 종료될 때 어떤 함수를 호출했는지, 현재의 피보나치 수 출력
d = [0] * 100

def pibo(x):
    print('f('+str(x)+')', end=' ')
    
    if x==1 or x==2:
        return 1
    
    if d[x] != 0:
        return d[x]
    
    d[x] = pibo(x-1) + pibo(x-2)
    return d[x]

pibo(6)
```

<br><br>

## Botton-Up DP
    반복문 이용
    ; 작은 문제부터 차근차근 답 도출
- 전형적인 DP

<br>
    
### 소스코드 (반복문) : 바텀업 방식 

```python
d  = [0] * 100 #DP 테이블 초기화

d[1] = 1
d[2] = 2
n = 99

#피보나치 함수를 반복문으로 구현(Bottom-Up DP)
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
    
print(d[n])
```
