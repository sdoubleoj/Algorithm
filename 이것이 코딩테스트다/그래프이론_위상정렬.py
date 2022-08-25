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
from collections import deque


v, e = map(int, input().split()) #노드 개수 v, 간선 개수 e

# 모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] * (v+1)

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트(그래프) 초기화
graph = [[] for i in range(v+1)]


# 방향 그래프의 모든 간선 정보 입력
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 A에서 B로 이동 가능
    indegree[b] += 1 # 진입차수 1 증가
    

# 위상 정렬 함수
def topology_sort():
    result = [] #알고리즘 수행 결과 담을 리스트
    q = deque() #큐 기능을 위한 deque 라이브러리 사용
    
    #처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
            
    #큐가 빌 때까지 반복
    while q:
        now = q.popleft() #큐에서 원소 꺼내기
        result.append(now)
        
        #해당 원소와 연결된 노드들의 진입차수에서 1 빼기
        for i in graph[now]:
            indegree[i] -+ 1
            #새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
        
        #위상정렬 수행 결과 출력
        for i in result:
            print(i, end=' ')


topology_sort()
