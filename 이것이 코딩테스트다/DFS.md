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

# 탐색 Search
- 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
- 그래프, 트리 등의 자료구조 내 탐색 

<대표 알고리즘>
- DFS
- BFS


# DFS, Depth-First Search, 깊이 우선 탐색 알고리즘
- 그래프에서 깊은 부분을 우선적으로 탐색
- **Stack 자료구조 이용**


## basic structure of **Graph**
< 구성 >
- 노드 Node == 정점 Vertex
- 간선 Edge

> 그래프 탐색 == 하나의 노드를 시작으로 다수의 노드 방문하는 것

- if 두 노드가 간선으로 연결: '두 노드는 인접하다(Adjacent)'


### 표현 방식


#### 인접 행렬 (Adjacency Matrix)
- **2차원 배열**(2차원 리스트)로 그래프의 연결 관계를 표현
    - 각 노드가 연결된 형태 기록
        - 연결되어 있지 않은 노드끼리는 '무한Infinity의 비용' 작성
        - 실제 코드에서 논리적으로 정답이 될 수 없는 큰 값을 999999999 or 987654321로 초기화하는 경우 많음


![Adjacency Matrix](./Adjacency_Matrix.png)

```python
INF = 999999999 #무한의 비용 선언 (987654321로 초기화하기도 함)

# 2차원 리스트를 이용해 인접 행렬 표현
graph = [
    [6, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)
```

#### 인접 리스트 Adjacent List
- **리스트**로 그래프의 연결 관계를 표현
- 모든 노드에 연결된 노드에 대한 정보를 차례대로 연결해 저장
- '연결 리스트' 자료구조로 구현
    - Python으로는 그냥 '2차원 리스트' 이용하면 됨 ('List 자료형'이 append() 메소드를 제공하므로, '배열Array'와 '연결 리스트Linked-List'의 기능을 기본 제공하기 때문)
<br>

![Adjacency List](./Adjacency_List.png)

```python
# row가 3개인 2차원 리스트로 인접 리스트 표현
graph = [ [] for _ in range(3)] #빈 2차원 리스트 생성

# 노드 0에 연결된 노드 정보 저장 (노드,거리)
graph[0].append((1,7))
graph[0].append((2,5))

# 노드 1에 연결된 노드 정보 저장 (노드,거리)
graph[1].append((0,7))

# 노드 2에 연결된 노드 정보 저장 (노드,거리)
graph[2].append((0,5))

print(graph)
```

#### **메모리** 및 **속도** 효율 비교

< 메모리 >
- 인접 리스트 방식 better
    : '인접 행렬 방식'은 모든 관계 저장 > 노드 개수가 많을 수록 메모리 낭비
    : '인접 리스트 방식'은 연결된 정보만을 저장 

< 노드 간 연결여부 확인 속도 >
- 인접 행렬 방식 better
    : '인접 리스트 방식'은 연결된 데이터를 하나씩 확인해야 함
    : '인접 행렬 방식'은 graph[1][7]만 확인하면 됨

=> 특정한 노드와 연결된 '모든' 인접 노드를 순회해야 하는 경우, '인접 리스트 방식'이 메모리 공간 낭비 적음


## 동작 과정

> 특정한 경로로 탐색하다가, 특정한 상황에서 최대한 깊숙이 들어가서 노드를 방문한 후, 다시 돌아가 다른 경로로 탐색

1. 탐색 시작 노드를 스택에 삽입하고 방문처리
<br>

2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면, 그 인접 노드를 스택에 넣고 방문처리. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
<br>

3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복.
<br>

** '방문처리': 스택에 한 번 삽입되어 처리된 노드가 다시 삽입되지 않게 체크하는 것. 각 노드를 한 번씩만 처리할 수 있게 됨.

```python

```
