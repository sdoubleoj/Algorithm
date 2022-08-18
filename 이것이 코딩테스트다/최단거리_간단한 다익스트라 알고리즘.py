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
import sys
input = sys.stdin.readline #일반 노트북 환경에서는 ValueError 발생 주의
INF = int(1e9)


n, m = map(int, input().split()) #노드 개수, 간선 개수
start = int(input()) #시작노드(인덱스)
graph = [ [] for i in range(n+1) ] #각 노드의 연결노드에 대한 정보를 담는 리스트
visited = [False] * (n+1) #방문 체크 리스트
distance = [INF] * (n+1) #최단 거리 테이블(1차원 리스트), 무한으로 초기화


#모든 간선 정보 입력받기
for _ in range(m):
    a, b, c = map(int, input().split()) #a번 노드에서 연결된 b노드로 가는 비용이 c
    graph[a].append((b,c))
    
    
#방문하지 않은 노드 중에서, 가장 최단 거리가 짧은 노드의 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0 #가장 최단 거리가 짧은 노드(인덱스) 
    
    for i in range(1, n+1): #모든 노드에 대해
        #노드i까지의 최단거리가 현재까지의 최단거리보다 짧고, 방문하지 않은 노드라면
        if distance[i] < min_value and not visited[i]: 
            min_value = distance[i] #최단 거리 갱신
            index = i #가장 최단 거리가 짧은 노드 갱신
    return index


def dijstra(start):
    #시작 노드에 대해 초기화
    distance[start] = 0 #시작 노드에서 시작 노드까지의 거리는 0
    visited[start] = True
    for j in graph[start]: #시작 노드에 연결되어 있는 노드 : (연결노드, 비용)
        distance[j[0]] = j[1] #j[0]: 연결노드(인덱스), j[1]: 비용(거리)
    
    #시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        #현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
    
    #현재 노드와 연결된 다른 노드 확인
    for j in graph[now]:
        cost = distance[now] + j[1] #현재 노드까지의 최단거리 + 현재 노드에서 연결노드까지의 거리
        
        #현재 노드를 거쳐 다른 노드로 이동하는 거리가 더 짧은 경우
        if cost < distance[j[0]]: 
            distance[j[0]] = cost
            

#다익스트라 알고리즘 실행
dijstra(start)


#모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    #도달할 수 없는 경우
    if distance[i] == INF :
        print('INFINITY')
    #도달할 수 있는 경우
    else:
        print(distance[i])
