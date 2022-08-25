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
import copy


v = int(input()) #듣고자 하는 강의의 수(노드) 개수
indegree = [0] * (v+1) #모든 노드에 대한 진입차수(선수관계)는 0으로 초기화
graph = [[] for _ in range(v+1)] #각 노드에 연결된 간선 정보 담기 위한 연결 리스트(그래프) 초기화
time = [0] * (v+1) #각 강의 시간을 0으로 초기화


# 방향 그래프의 모든 간선 정보 
for i in range(1, v+1): #1번 강의부터 v번 강의까지,
    data = list(map(int, input().split())) #각 강의의 강의시간, 선수 강의 번호, -1
    time[i] = data[0] #강의 시간
    for x in data[1:-1]: #선수 강의 번호
        indegree[i] += 1 #i번 강의의 진입차수(선수 강의 존재 여부)
        graph[x].append(i) # 방향성: X to I


# 위상 정렬 함수
def topology_sort():
    result = copy.deepcopy(time) #알고리즘 수행 결과 담을 리스트; 각 강의를 수강하기까지의 최종 최소 시간
    q = deque()
    
    
    #처음 시작할 때는 진입차수가 0인 노드를 먼저 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    
    
    #큐가 빌 때까지 반복
    while q:
        now = q.popleft() #큐에서 원소 꺼내기
        
        #해당 원소와 연결된 노드들의 진입차수에서 -1
        for i in graph[now]:
            result[i] = max(result[i], result[now]+time[i])
            indegree -= 1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] == 0:
                q.append(i)
    
    # 위상 정렬 수행 결과 출력
    for i in range(1, v+1):
        print(result[i])
        

topology_sort()
