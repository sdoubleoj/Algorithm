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
---
<br>

- 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
<br>

- **그래프**, **트리** 등의 자료구조 내 탐색
<br>

- 대표 알고리즘
<br>

    | |**DFS**|**BFS**|
    |------|------|------|
    |동작원리|Stack|Queue|
    |구현방법|재귀함수 이용|큐 자료구조 이용|

<br><br>




# DFS, Depth First Search, 깊이 우선 탐색 알고리즘
---
<br>

- 그래프에서 깊은(최대한 멀리 있는) 부분(노드)를 우선적으로 탐색
- **Stack 자료구조** 이용 알고리즘
- 시간 복잡도 $O(N)$

<br><br>




## basic structure of **Graph**
---
<br>

### 구성
- 노드 Node == 정점 Vertex
- 간선 Edge

> 그래프 탐색 == 하나의 노드를 시작으로 다수의 노드 방문하는 것

- if 두 노드가 간선으로 연결: '두 노드는 인접하다(Adjacent)'

<br><br>




### 표현 방식
<br>

#### 인접 행렬 (Adjacency Matrix)
- **2차원 배열**(2차원 리스트)로 그래프의 연결 관계를 표현
    - 각 노드가 연결된 형태 기록
        - 연결되어 있지 않은 노드끼리는 '무한Infinity의 비용' 작성
        - 실제 코드에서 논리적으로 정답이 될 수 없는 큰 값을 999999999 or 987654321로 초기화하는 경우 많음


![Adjacency Matrix](./Adjacency_Matrix.png)


#### 인접 행렬 예제

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

<!-- #region -->
<br><br>


#### 인접 리스트 Adjacent List
- **리스트**로 그래프의 연결 관계를 표현
- 모든 노드에 연결된 노드에 대한 정보를 차례대로 연결해 저장
- '연결 리스트' 자료구조로 구현
    - Python으로는 그냥 '2차원 리스트' 이용하면 됨 ('List 자료형'이 append() 메소드를 제공하므로, '배열Array'와 '연결 리스트Linked-List'의 기능을 기본 제공하기 때문)
<br>

![Adjacency List](./Adjacency_List.png)
<!-- #endregion -->

#### 인접 리스트 예제

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

<!-- #region -->
<br><br>


#### **메모리** 및 **속도** 효율 비교
<br>

< 메모리 >
- 인접 리스트 방식 better
    : '인접 행렬 방식'은 모든 관계 저장 > 노드 개수가 많을 수록 메모리 낭비
    : '인접 리스트 방식'은 연결된 정보만을 저장
    
<br>

< 노드 간 연결여부 확인 속도 >
- 인접 행렬 방식 better
    : '인접 리스트 방식'은 연결된 데이터를 하나씩 확인해야 함
    : '인접 행렬 방식'은 graph[1][7]만 확인하면 됨

     => 특정한 노드와 연결된 '모든' 인접 노드를 순회해야 하는 경우, '인접 리스트 방식'이 메모리 공간 낭비 적음
     
<br><br>



<!-- #endregion -->

## 동작 과정
---
<br>

> 특정한 경로로 탐색하다가, 특정한 상황에서 최대한 깊숙이 들어가서 노드를 방문한 후, 다시 돌아가 다른 경로로 탐색

1. 탐색 시작 노드를 스택에 삽입하고 방문처리
    - ** '방문처리': 스택에 한 번 삽입되어 처리된 노드가 다시 삽입되지 않게 체크하는 것. 각 노드를 한 번씩만 처리할 수 있게 됨.
<br>

2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면, 그 인접 노드를 스택에 넣고 방문처리. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼냄
<br>

3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복.
<br>

    => 노드 탐색 순서 : 스택에 들어간 순서


### DFS 예제

```python
#DFS 메서드 정의(인자: 노드 연결 정보, 현재 노드, 방문처리 여부)
def dfs(graph, v, visited):
    
    #현재 노드 방문처리
    visited[v] = True
    print(v, end=' ')
    
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]: #현재 노드에 인접한 노드 하나씩
        if not visited[i]: #방문하지 않은 노드면
            dfs(graph, i, visited) #그 노드 방문 진행

#각 노드가 연결된 정보(graph)를 리스트 자료형으로 표현 (2차원 리스트)
graph = [
    [], # idx 0은 비워둠
    [2,3,8], #1번 노드에 인접한 노드
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

#각 노드가 방문된 정보(visited)를 리스트 자료형으로 표현 (1차원 리스트) 
visited = [False] * 9 #idx 0을 사용하지 않기 위해 n+1인 9로 초기화

#정의된 DFS 함수 호출
dfs(graph, 1, visited)
```

<!-- #region -->
<br><br>

# BFS, Breadth First Search, 너비 우선 탐색
---
<br>

- 가까운 노드부터 탐색하는 알고리즘
- 큐Queue 자료구조 이용 (FIFO)
        => deque 라이브러리 사용
- 시간 복잡도 $O(N)\qquad$  (코테에서는 DFS 구현보다 빠르게 동작)

<br><br>



## 동작 과정
---
<br>

> 인접한 노드를 반복적으로 *큐*에 넣도록 알고리즘을 작성하면, 자연스럽게 먼저 나가게 되어 가까운 노드부터 탐색 진행하게 됨
<br>

1. 탐색 시작 노드를 *큐*에 삽입하고 방문처리
<br>

2. *큐*에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 *큐*에 삽입하고 방문처리
<br>

3. 2번을 더 이상 수행할 수 없을 때까지 반복
<br>
    => 노드 탐색 순서 : 큐에 들어간 순서
    
<br><br>

<!-- #endregion -->

### BFS 예제

```python
from collections import deque

#define DFS method
def bfs(graph, start, visited):
    
    #큐 구현을 위해 deque 라이브러리 사용
    queue = deque([start]) #큐에 현재 노드 삽입
    
    #현재 노드 방문 처리
    visited[start] = True
    
    #큐가 빌 때까지 반복
    while True:
        #큐에서 아래쪽 노드를 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        
        #해당 노드와 연결된, 아직 방문하지 않은 노드들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]: #방문하지 않은 노드면
                queue.append(i) #큐에 삽입하고
                visited[i] = True #방문처리

#각 노드가 연결된 정보(graph)를 숫자가 작은 노드부터 리스트 자료형으로 표현 (2차원 리스트)
graph = [
    [], # idx 0은 비워둠
    [2,3,8], #1번 노드에 인접한 노드
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

#각 노드가 방문된 정보(visited)를 리스트 자료형으로 표현 (1차원 리스트) 
visited = [False] * 9 #idx 0을 사용하지 않기 위해 n+1인 9로 초기화

#정의된 DFS 함수 호출
bfs(graph, 1, visited)
```

# 코테 tip
<br>

- 2차원 배열에서의 탐색 문제를 만나면 모든 좌표 형태를 위와 같은 그래프 형태로 바꿔서 풀이  
<br>

    ex. 게임 맵이 3x3 형태의 2차원 배열, 각 데이터는 좌표, 각 좌표를 상하좌우로만 이동가능
