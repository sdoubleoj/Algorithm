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

# 최단 경로
---
  
- 특정 지점까지 가장 빠르게 도달하는 방법을 찾는 알고리즘
- 그래프로 표현 ..  각 지점 = 노드 | 지점간 연결 도로 = 간선
- 그리디 & 다이나믹 프로그래밍 알고리즘이 그대로 적용됨



<br><br>

# 다익스트라(데이크스트라) 알고리즘, Dijkstra
---
- 그래프에서 여러 개의 노드가 있을 때, 특정환 노드에서 출발하여 다른 노드로 가는 각각의 최단 경로를 구해주는 알고리즘  
  
- '음의 간선(0보다 작은 값을 가지는 간선)'이 없어야 함 (GPS SW 기본 알고리즘)  
  
- 그리디 알고리즘으로 분류  
    : 매번 '가장 비용이 적은 노드'를 선택해서 임의의 과정 반복함  
      
- 동작 원리
    1. 출발 노드 설정
    2. 최단 거리 테이블(1차원 리스트) '무한'으로 초기화   
        ex) int(1e9) 등 (파이썬은 1e9를 실수형으로 처리함)  
    3. 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택
    4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단 거리 테이블 갱신
    5. 3 & 4번 반복(Greedy Point)
  ** 한 번 선택된 노드는 최단 거리가 감소하지 않음, 즉 다익스트라는 "한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾음"



<br><br>
## Basic ver.
  
- 시간 복잡도 : $O(V^2) \quad$ ( V: 노드 개수 )
- 매 단계마다 최단 거리 테이블의 모든 원소 확인 (순차 탐색)

 \**코테에서 보통 노드간 '최단 거리'만 출력 요청
 
<br>

```python
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split()) #노드 개수, 간선 개수
start = int(input())
graph = [ [] for i in range(n+1) ]
visited = [False] * (n+1)
distance = [INF] * (n+1) #최단 거리 테이블(1차원 리스트)

#모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split()) #a번 노드에서 연결된 b노드로 가는 비용이 c
    graph[a].append((b,c))
    


    

```

```python
import sys
#input = sys.stdin.readline #일반 노트북 환경에서는 ValueError 발생
INF = int(1e9)

n, m = 6, 11 #노드 개수, 간선 개수
start = 1 #시작 노드 번호
graph = [ [] for i in range(n+1) ] #각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
visited = [False] * (n+1) #방문한 적이 있는지 체크하는 목적의 리스트
distance = [INF] * (n+1) #최단 거리 테이블을 모두 무한으로 초기화

```

```python
#모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b,c)) #노드a에서 노드b로 가는 비용이 c
```

```python
graph = [ [] for i in range(5) ];graph
```

```python
graph[1].append((2,3))
```


## Improved ver.


# 플로이드 워셜 알고리즘, Floyd-Warshall
